use polars_core::prelude::*;

use crate::logical_plan::projection_expr::ProjectionExprs;
use crate::prelude::*;

pub(super) struct SlicePushDown {
    streaming: bool,
    pub scratch: Vec<Node>,
}

#[derive(Copy, Clone)]
struct State {
    offset: i64,
    len: IdxSize,
}

/// Can push down slice when:
/// * all projections are elementwise
/// * at least 1 projection is based on a column (for height broadcast)
/// * projections not based on any column project as scalars
///
/// Returns (all_elementwise, all_elementwise_and_any_expr_has_column)
fn can_pushdown_slice_past_projections(
    exprs: &ProjectionExprs,
    arena: &Arena<AExpr>,
) -> (bool, bool) {
    let mut all_elementwise_and_any_expr_has_column = false;
    for node in exprs.iter() {
        // `select(c = Literal([1, 2, 3])).slice(0, 0)` must block slice pushdown,
        // because `c` projects to a height independent from the input height. We check
        // this by observing that `c` does not have any columns in its input notes.
        //
        // TODO: Simply checking that a column node is present does not handle e.g.:
        // `select(c = Literal([1, 2, 3]).is_in(col(a)))`, for functions like `is_in`,
        // `str.contains`, `str.contains_many` etc. - observe a column node is present
        // but the output height is not dependent on it.
        let mut has_column = false;
        let mut literals_all_scalar = true;
        let is_elementwise = arena.iter(*node).all(|(_node, ae)| {
            has_column |= matches!(ae, AExpr::Column(_));
            literals_all_scalar &= if let AExpr::Literal(v) = ae {
                v.projects_as_scalar()
            } else {
                true
            };
            single_aexpr_is_elementwise(ae)
        });

        // If there is no column then all literals must be scalar
        if !is_elementwise || !(has_column || literals_all_scalar) {
            return (false, false);
        }

        all_elementwise_and_any_expr_has_column |= has_column
    }

    (true, all_elementwise_and_any_expr_has_column)
}

impl SlicePushDown {
    pub(super) fn new(streaming: bool) -> Self {
        Self {
            streaming,
            scratch: vec![],
        }
    }

    // slice will be done at this node if we found any
    // we also stop optimization
    fn no_pushdown_finish_opt(
        &self,
        lp: ALogicalPlan,
        state: Option<State>,
        lp_arena: &mut Arena<ALogicalPlan>,
    ) -> PolarsResult<ALogicalPlan> {
        match state {
            Some(state) => {
                let input = lp_arena.add(lp);

                let lp = ALogicalPlan::Slice {
                    input,
                    offset: state.offset,
                    len: state.len,
                };
                Ok(lp)
            },
            None => Ok(lp),
        }
    }

    /// slice will be done at this node, but we continue optimization
    fn no_pushdown_restart_opt(
        &self,
        lp: ALogicalPlan,
        state: Option<State>,
        lp_arena: &mut Arena<ALogicalPlan>,
        expr_arena: &mut Arena<AExpr>,
    ) -> PolarsResult<ALogicalPlan> {
        let inputs = lp.get_inputs();
        let exprs = lp.get_exprs();

        let new_inputs = inputs
            .iter()
            .map(|&node| {
                let alp = lp_arena.take(node);
                // No state, so we do not push down the slice here.
                let state = None;
                let alp = self.pushdown(alp, state, lp_arena, expr_arena)?;
                lp_arena.replace(node, alp);
                Ok(node)
            })
            .collect::<PolarsResult<Vec<_>>>()?;
        let lp = lp.with_exprs_and_input(exprs, new_inputs);

        self.no_pushdown_finish_opt(lp, state, lp_arena)
    }

    /// slice will be pushed down.
    fn pushdown_and_continue(
        &self,
        lp: ALogicalPlan,
        state: Option<State>,
        lp_arena: &mut Arena<ALogicalPlan>,
        expr_arena: &mut Arena<AExpr>,
    ) -> PolarsResult<ALogicalPlan> {
        let inputs = lp.get_inputs();
        let exprs = lp.get_exprs();

        let new_inputs = inputs
            .iter()
            .map(|&node| {
                let alp = lp_arena.take(node);
                let alp = self.pushdown(alp, state, lp_arena, expr_arena)?;
                lp_arena.replace(node, alp);
                Ok(node)
            })
            .collect::<PolarsResult<Vec<_>>>()?;
        Ok(lp.with_exprs_and_input(exprs, new_inputs))
    }

    fn pushdown(
        &self,
        lp: ALogicalPlan,
        state: Option<State>,
        lp_arena: &mut Arena<ALogicalPlan>,
        expr_arena: &mut Arena<AExpr>,
    ) -> PolarsResult<ALogicalPlan> {
        use ALogicalPlan::*;

        match (lp, state) {
            #[cfg(feature = "python")]
            (PythonScan {
                mut options,
                predicate,
            },
            // TODO! we currently skip slice pushdown if there is a predicate.
            // we can modify the readers to only limit after predicates have been applied
                Some(state)) if state.offset == 0 && predicate.is_none() => {
                options.n_rows = Some(state.len as usize);
                let lp = PythonScan {
                    options,
                    predicate
                };
                Ok(lp)
            }
            #[cfg(feature = "csv")]
            (Scan {
                paths,
                file_info,
                output_schema,
                file_options: mut options,
                predicate,
                scan_type: FileScan::Csv {options: mut csv_options}
            }, Some(state)) if predicate.is_none() && state.offset >= 0 =>  {
                options.n_rows = Some(state.len as usize);
                csv_options.skip_rows += state.offset as usize;

                let lp = Scan {
                    paths,
                    file_info,
                    output_schema,
                    scan_type: FileScan::Csv {options: csv_options},
                    file_options: options,
                    predicate,
                };
                Ok(lp)
            },
            // TODO! we currently skip slice pushdown if there is a predicate.
            (Scan {
                paths,
                file_info,
                output_schema,
                file_options: mut options,
                predicate,
                scan_type
            }, Some(state)) if state.offset == 0 && predicate.is_none() => {
                options.n_rows = Some(state.len as usize);
                let lp = Scan {
                    paths,
                    file_info,
                    output_schema,
                    predicate,
                    file_options: options,
                    scan_type
                };

                Ok(lp)
            }
            (Union {mut inputs, mut options }, Some(state)) => {
                options.slice = Some((state.offset, state.len as usize));
                if state.offset == 0 {
                    for input in &mut inputs {
                        let input_lp = lp_arena.take(*input);
                        let input_lp = self.pushdown(input_lp, Some(state), lp_arena, expr_arena)?;
                        lp_arena.replace(*input, input_lp);
                    }
                }
                Ok(Union {inputs, options})
            },
            (Join {
                input_left,
                input_right,
                schema,
                left_on,
                right_on,
                mut options
            }, Some(state)) if !self.streaming => {
                // first restart optimization in both inputs and get the updated LP
                let lp_left = lp_arena.take(input_left);
                let lp_left = self.pushdown(lp_left, None, lp_arena, expr_arena)?;
                let input_left = lp_arena.add(lp_left);

                let lp_right = lp_arena.take(input_right);
                let lp_right = self.pushdown(lp_right, None, lp_arena, expr_arena)?;
                let input_right = lp_arena.add(lp_right);

                // then assign the slice state to the join operation

                let mut_options = Arc::make_mut(&mut options);
                mut_options.args.slice = Some((state.offset, state.len as usize));

                Ok(Join {
                    input_left,
                    input_right,
                    schema,
                    left_on,
                    right_on,
                    options
                })
            }
            (Aggregate { input, keys, aggs, schema, apply, maintain_order, mut options }, Some(state)) => {
                // first restart optimization in inputs and get the updated LP
                let input_lp = lp_arena.take(input);
                let input_lp = self.pushdown(input_lp, None, lp_arena, expr_arena)?;
                let input= lp_arena.add(input_lp);

                let mut_options= Arc::make_mut(&mut options);
                mut_options.slice = Some((state.offset, state.len as usize));

                Ok(Aggregate {
                    input,
                    keys,
                    aggs,
                    schema,
                    apply,
                    maintain_order,
                    options
                })
            }
            (Distinct {input, mut options}, Some(state)) => {
                // first restart optimization in inputs and get the updated LP
                let input_lp = lp_arena.take(input);
                let input_lp = self.pushdown(input_lp, None, lp_arena, expr_arena)?;
                let input= lp_arena.add(input_lp);
                options.slice = Some((state.offset, state.len as usize));
                Ok(Distinct {
                    input,
                    options,
                })
            }
            (Sort {input, by_column, mut args}, Some(state)) => {
                // first restart optimization in inputs and get the updated LP
                let input_lp = lp_arena.take(input);
                let input_lp = self.pushdown(input_lp, None, lp_arena, expr_arena)?;
                let input= lp_arena.add(input_lp);

                args.slice = Some((state.offset, state.len as usize));
                Ok(Sort {
                    input,
                    by_column,
                    args
                })
            }
            (Slice {
                input,
                offset,
                len
            }, Some(previous_state)) => {
                let alp = lp_arena.take(input);
                let state = Some(if previous_state.offset == offset  {
                    State {
                        offset,
                        len: std::cmp::min(len, previous_state.len)
                    }
                } else {
                    State {
                        offset,
                        len
                    }
                });
                let lp = self.pushdown(alp, state, lp_arena, expr_arena)?;
                let input = lp_arena.add(lp);
                Ok(Slice {
                    input,
                    offset: previous_state.offset,
                    len: previous_state.len
                })
            }
            (Slice {
                input,
                offset,
                len
            }, None) => {
                let alp = lp_arena.take(input);
                let state = Some(State {
                    offset,
                    len
                });
                self.pushdown(alp, state, lp_arena, expr_arena)
            }
            // [Do not pushdown] boundary
            // here we do not pushdown.
            // we reset the state and then start the optimization again
            m @ (Selection { .. }, _)
            // other blocking nodes
            | m @ (DataFrameScan {..}, _)
            | m @ (Sort {..}, _)
            | m @ (MapFunction {function: FunctionNode::Explode {..}, ..}, _)
            | m @ (MapFunction {function: FunctionNode::Melt {..}, ..}, _)
            | m @ (Cache {..}, _)
            | m @ (Distinct {..}, _)
            | m @ (Aggregate{..},_)
            // blocking in streaming
            | m @ (Join{..},_)
            => {
                let (lp, state) = m;
                self.no_pushdown_restart_opt(lp, state, lp_arena, expr_arena)
            }
            // [Pushdown]
            (MapFunction {input, function}, _) if function.allow_predicate_pd() => {
                let lp = MapFunction {input, function};
                self.pushdown_and_continue(lp, state, lp_arena, expr_arena)
            },
            // [NO Pushdown]
            m @ (MapFunction {..}, _) => {
                let (lp, state) = m;
                self.no_pushdown_restart_opt(lp, state, lp_arena, expr_arena)
            }
            // [Pushdown]
            // these nodes will be pushed down.
             // State is None, we can continue
             m @(Projection{..}, None)
            => {
                let (lp, state) = m;
                self.pushdown_and_continue(lp, state, lp_arena, expr_arena)
            }
            // there is state, inspect the projection to determine how to deal with it
            (Projection {input, expr, schema, options}, Some(_)) => {
                if can_pushdown_slice_past_projections(&expr, expr_arena).1 {
                    let lp = Projection {input, expr, schema, options};
                    self.pushdown_and_continue(lp, state, lp_arena, expr_arena)
                }
                // don't push down slice, but restart optimization
                else {
                    let lp = Projection {input, expr, schema, options};
                    self.no_pushdown_restart_opt(lp, state, lp_arena, expr_arena)
                }
            }
            (HStack {input, exprs, schema, options}, _) => {
                let check = can_pushdown_slice_past_projections(&exprs, expr_arena);

                if (
                    // If the schema length is greater then an input column is being projected, so
                    // the exprs in with_columns do not need to have an input column name.
                    schema.len() > exprs.len() && check.0
                )
                || check.1 // e.g. select(c).with_columns(c = c + 1)
                {
                    let lp = HStack {input, exprs, schema, options};
                    self.pushdown_and_continue(lp, state, lp_arena, expr_arena)
                }
                // don't push down slice, but restart optimization
                else {
                    let lp = HStack {input, exprs, schema, options};
                    self.no_pushdown_restart_opt(lp, state, lp_arena, expr_arena)
                }
            }
            (HConcat {inputs, schema, options}, _) => {
                // Slice can always be pushed down for horizontal concatenation
                let lp = HConcat {inputs, schema, options};
                self.pushdown_and_continue(lp, state, lp_arena, expr_arena)
            }
            (catch_all, state) => {
                self.no_pushdown_finish_opt(catch_all, state, lp_arena)
            }

        }
    }

    pub fn optimize(
        &self,
        logical_plan: ALogicalPlan,
        lp_arena: &mut Arena<ALogicalPlan>,
        expr_arena: &mut Arena<AExpr>,
    ) -> PolarsResult<ALogicalPlan> {
        self.pushdown(logical_plan, None, lp_arena, expr_arena)
    }
}
