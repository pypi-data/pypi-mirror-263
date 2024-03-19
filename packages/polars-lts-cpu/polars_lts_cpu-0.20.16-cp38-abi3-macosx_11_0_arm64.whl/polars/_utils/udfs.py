"""Utilities related to user defined functions (such as those passed to `apply`)."""

from __future__ import annotations

import datetime
import dis
import inspect
import re
import sys
import warnings
from bisect import bisect_left
from collections import defaultdict
from dis import get_instructions
from inspect import signature
from itertools import count, zip_longest
from pathlib import Path
from typing import (
    TYPE_CHECKING,
    AbstractSet,
    Any,
    Callable,
    ClassVar,
    Iterator,
    Literal,
    NamedTuple,
    Union,
)

from polars._utils.various import re_escape

if TYPE_CHECKING:
    from dis import Instruction

    if sys.version_info >= (3, 10):
        from typing import TypeAlias
    else:
        from typing_extensions import TypeAlias


class StackValue(NamedTuple):
    operator: str
    operator_arity: int
    left_operand: str
    right_operand: str


MapTarget: TypeAlias = Literal["expr", "frame", "series"]
StackEntry: TypeAlias = Union[str, StackValue]

_MIN_PY311 = sys.version_info >= (3, 11)
_MIN_PY312 = _MIN_PY311 and sys.version_info >= (3, 12)


class OpNames:
    BINARY: ClassVar[dict[str, str]] = {
        "BINARY_ADD": "+",
        "BINARY_AND": "&",
        "BINARY_FLOOR_DIVIDE": "//",
        "BINARY_LSHIFT": "<<",
        "BINARY_RSHIFT": ">>",
        "BINARY_MODULO": "%",
        "BINARY_MULTIPLY": "*",
        "BINARY_OR": "|",
        "BINARY_POWER": "**",
        "BINARY_SUBTRACT": "-",
        "BINARY_TRUE_DIVIDE": "/",
        "BINARY_XOR": "^",
    }
    CALL = frozenset({"CALL"} if _MIN_PY311 else {"CALL_FUNCTION", "CALL_METHOD"})
    CONTROL_FLOW: ClassVar[dict[str, str]] = (
        {
            "POP_JUMP_FORWARD_IF_FALSE": "&",
            "POP_JUMP_FORWARD_IF_TRUE": "|",
            "JUMP_IF_FALSE_OR_POP": "&",
            "JUMP_IF_TRUE_OR_POP": "|",
        }
        # note: 3.12 dropped POP_JUMP_FORWARD_IF_* opcodes
        if _MIN_PY311 and not _MIN_PY312
        else {
            "POP_JUMP_IF_FALSE": "&",
            "POP_JUMP_IF_TRUE": "|",
            "JUMP_IF_FALSE_OR_POP": "&",
            "JUMP_IF_TRUE_OR_POP": "|",
        }
    )
    LOAD_VALUES = frozenset(("LOAD_CONST", "LOAD_DEREF", "LOAD_FAST", "LOAD_GLOBAL"))
    LOAD_ATTR = frozenset({"LOAD_METHOD", "LOAD_ATTR"})
    LOAD = LOAD_VALUES | LOAD_ATTR
    SYNTHETIC: ClassVar[dict[str, int]] = {
        "POLARS_EXPRESSION": 1,
    }
    UNARY: ClassVar[dict[str, str]] = {
        "UNARY_NEGATIVE": "-",
        "UNARY_POSITIVE": "+",
        "UNARY_NOT": "~",
    }
    PARSEABLE_OPS = frozenset(
        {"BINARY_OP", "BINARY_SUBSCR", "COMPARE_OP", "CONTAINS_OP", "IS_OP"}
        | set(UNARY)
        | set(CONTROL_FLOW)
        | set(SYNTHETIC)
        | LOAD_VALUES
    )
    UNARY_VALUES = frozenset(UNARY.values())


# numpy functions that we can map to native expressions
_NUMPY_MODULE_ALIASES = frozenset(("np", "numpy"))
_NUMPY_FUNCTIONS = frozenset(
    (
        # "abs",  # TODO: this one clashes with Python builtin abs
        "arccos",
        "arccosh",
        "arcsin",
        "arcsinh",
        "arctan",
        "arctanh",
        "cbrt",
        "ceil",
        "cos",
        "cosh",
        "degrees",
        "exp",
        "floor",
        "log",
        "log10",
        "log1p",
        "radians",
        "sign",
        "sin",
        "sinh",
        "sqrt",
        "tan",
        "tanh",
    )
)

# python attrs/funcs that map to native expressions
_PYTHON_ATTRS_MAP = {
    "date": "dt.date()",
    "day": "dt.day()",
    "hour": "dt.hour()",
    "microsecond": "dt.microsecond()",
    "minute": "dt.minute()",
    "month": "dt.month()",
    "second": "dt.second()",
    "year": "dt.year()",
}
_PYTHON_CASTS_MAP = {"float": "Float64", "int": "Int64", "str": "String"}
_PYTHON_BUILTINS = frozenset(_PYTHON_CASTS_MAP) | {"abs"}
_PYTHON_METHODS_MAP = {
    # string
    "endswith": "str.ends_with",
    "lower": "str.to_lowercase",
    "lstrip": "str.strip_chars_start",
    "rstrip": "str.strip_chars_end",
    "startswith": "str.starts_with",
    "strip": "str.strip_chars",
    "title": "str.to_titlecase",
    "upper": "str.to_uppercase",
    # temporal
    "date": "dt.date",
    "isoweekday": "dt.weekday",
    "time": "dt.time",
}

_MODULE_FUNCTIONS: list[dict[str, list[AbstractSet[str]]]] = [
    # lambda x: numpy.func(x)
    # lambda x: numpy.func(CONSTANT)
    {
        "argument_1_opname": [{"LOAD_FAST", "LOAD_CONST"}],
        "argument_2_opname": [],
        "module_opname": [OpNames.LOAD_ATTR],
        "attribute_opname": [],
        "module_name": [_NUMPY_MODULE_ALIASES],
        "attribute_name": [],
        "function_name": [_NUMPY_FUNCTIONS],
    },
    # lambda x: json.loads(x)
    {
        "argument_1_opname": [{"LOAD_FAST"}],
        "argument_2_opname": [],
        "module_opname": [OpNames.LOAD_ATTR],
        "attribute_opname": [],
        "module_name": [{"json"}],
        "attribute_name": [],
        "function_name": [{"loads"}],
    },
    # lambda x: datetime.strptime(x, CONSTANT)
    {
        "argument_1_opname": [{"LOAD_FAST"}],
        "argument_2_opname": [{"LOAD_CONST"}],
        "module_opname": [OpNames.LOAD_ATTR],
        "attribute_opname": [],
        "module_name": [{"datetime"}],
        "attribute_name": [],
        "function_name": [{"strptime"}],
    },
    # lambda x: module.attribute.func(x, CONSTANT)
    {
        "argument_1_opname": [{"LOAD_FAST"}],
        "argument_2_opname": [{"LOAD_CONST"}],
        "module_opname": [{"LOAD_ATTR"}],
        "attribute_opname": [OpNames.LOAD_ATTR],
        "module_name": [{"datetime", "dt"}],
        "attribute_name": [{"datetime"}],
        "function_name": [{"strptime"}],
    },
]
# In addition to `lambda x: func(x)`, also support cases when a unary operation
# has been applied to `x`, like `lambda x: func(-x)` or `lambda x: func(~x)`.
_MODULE_FUNCTIONS = [
    {**kind, "argument_1_unary_opname": unary}  # type: ignore[dict-item]
    for kind in _MODULE_FUNCTIONS
    for unary in [[set(OpNames.UNARY)], []]
]
_RE_IMPLICIT_BOOL = re.compile(r'pl\.col\("([^"]*)"\) & pl\.col\("\1"\)\.(.+)')


def _get_all_caller_variables() -> dict[str, Any]:
    """Get all local and global variables from caller's frame."""
    pkg_dir = Path(__file__).parent.parent

    # https://stackoverflow.com/questions/17407119/python-inspect-stack-is-slow
    frame = inspect.currentframe()
    n = 0
    try:
        while frame:
            fname = inspect.getfile(frame)
            if fname.startswith(str(pkg_dir)):
                frame = frame.f_back
                n += 1
            else:
                break
        variables: dict[str, Any]
        if frame is None:
            variables = {}
        else:
            variables = {**frame.f_locals, **frame.f_globals}
    finally:
        # https://docs.python.org/3/library/inspect.html
        # > Though the cycle detector will catch these, destruction of the frames
        # > (and local variables) can be made deterministic by removing the cycle
        # > in a finally clause.
        del frame
    return variables


class BytecodeParser:
    """Introspect UDF bytecode and determine if we can rewrite as native expression."""

    _map_target_name: str | None = None

    def __init__(self, function: Callable[[Any], Any], map_target: MapTarget):
        try:
            original_instructions = get_instructions(function)
        except TypeError:
            # in case we hit something that can't be disassembled (eg: code object
            # unavailable, like a bare numpy ufunc that isn't in a lambda/function)
            original_instructions = iter([])

        self._function = function
        self._map_target = map_target
        self._param_name = self._get_param_name(function)
        self._rewritten_instructions = RewrittenInstructions(
            instructions=original_instructions,
        )

    def _omit_implicit_bool(self, expr: str) -> str:
        """Drop extraneous/implied bool (eg: `pl.col("d") & pl.col("d").dt.date()`)."""
        while _RE_IMPLICIT_BOOL.search(expr):
            expr = _RE_IMPLICIT_BOOL.sub(repl=r'pl.col("\1").\2', string=expr)
        return expr

    @staticmethod
    def _get_param_name(function: Callable[[Any], Any]) -> str | None:
        """Return single function parameter name."""
        try:
            # note: we do not parse/handle functions with > 1 params
            sig = signature(function)
        except ValueError:
            return None
        return (
            next(iter(parameters.keys()))
            if len(parameters := sig.parameters) == 1
            else None
        )

    def _inject_nesting(
        self,
        expression_blocks: dict[int, str],
        logical_instructions: list[Instruction],
    ) -> list[tuple[int, str]]:
        """Inject nesting boundaries into expression blocks (as parentheses)."""
        if logical_instructions:
            # reconstruct nesting boundaries for mixed and/or ops by associating control
            # flow jump offsets with their target expression blocks and applying parens
            if len({inst.opname for inst in logical_instructions}) > 1:
                block_offsets: list[int] = list(expression_blocks.keys())
                prev_end = -1
                for inst in logical_instructions:
                    start = block_offsets[bisect_left(block_offsets, inst.offset) - 1]
                    end = block_offsets[bisect_left(block_offsets, inst.argval) - 1]
                    if not (start == 0 and end == block_offsets[-1]):
                        if prev_end not in (start, end):
                            expression_blocks[start] = "(" + expression_blocks[start]
                            expression_blocks[end] += ")"
                            prev_end = end

            for inst in logical_instructions:  # inject connecting "&" and "|" ops
                expression_blocks[inst.offset] = OpNames.CONTROL_FLOW[inst.opname]

        return sorted(expression_blocks.items())

    def _get_target_name(self, col: str, expression: str) -> str:
        """The name of the object against which the 'map' is being invoked."""
        if self._map_target_name is not None:
            return self._map_target_name
        else:
            col_expr = f'pl.col("{col}")'
            if self._map_target == "expr":
                return col_expr
            elif self._map_target == "series":
                # note: handle overlapping name from global variables; fallback
                # through "s", "srs", "series" and (finally) srs0 -> srsN...
                search_expr = expression.replace(col_expr, "")
                for name in ("s", "srs", "series"):
                    if not re.search(rf"\b{name}\b", search_expr):
                        self._map_target_name = name
                        return name
                n = count()
                while True:
                    name = f"srs{next(n)}"
                    if not re.search(rf"\b{name}\b", search_expr):
                        self._map_target_name = name
                        return name

        msg = f"TODO: map_target = {self._map_target!r}"
        raise NotImplementedError(msg)

    @property
    def map_target(self) -> MapTarget:
        """The map target, eg: one of 'expr', 'frame', or 'series'."""
        return self._map_target

    def can_attempt_rewrite(self) -> bool:
        """
        Determine if we may be able to offer a native polars expression instead.

        Note that `lambda x: x` is inefficient, but we ignore it because it is not
        guaranteed that using the equivalent bare constant value will return the
        same output. (Hopefully nobody is writing lambdas like that anyway...)
        """
        return (
            self._param_name is not None
            # check minimum number of ops, ensuring all are parseable
            and len(self._rewritten_instructions) >= 2
            and all(
                inst.opname in OpNames.PARSEABLE_OPS
                for inst in self._rewritten_instructions
            )
            # exclude constructs/functions with multiple RETURN_VALUE ops
            and sum(
                1
                for inst in self.original_instructions
                if inst.opname == "RETURN_VALUE"
            )
            == 1
        )

    def dis(self) -> None:
        """Print disassembled function bytecode."""
        dis.dis(self._function)

    @property
    def function(self) -> Callable[[Any], Any]:
        """The function being parsed."""
        return self._function

    @property
    def original_instructions(self) -> list[Instruction]:
        """The original bytecode instructions from the function we are parsing."""
        return list(self._rewritten_instructions._original_instructions)

    @property
    def param_name(self) -> str | None:
        """The parameter name of the function being parsed."""
        return self._param_name

    @property
    def rewritten_instructions(self) -> list[Instruction]:
        """The rewritten bytecode instructions from the function we are parsing."""
        return list(self._rewritten_instructions)

    def to_expression(self, col: str) -> str | None:
        """Translate postfix bytecode instructions to polars expression/string."""
        self._map_target_name = None
        if self._param_name is None:
            return None

        # decompose bytecode into logical 'and'/'or' expression blocks (if present)
        control_flow_blocks = defaultdict(list)
        logical_instructions = []
        jump_offset = 0
        for idx, inst in enumerate(self._rewritten_instructions):
            if inst.opname in OpNames.CONTROL_FLOW:
                jump_offset = self._rewritten_instructions[idx + 1].offset
                logical_instructions.append(inst)
            else:
                control_flow_blocks[jump_offset].append(inst)

        # convert each block to a polars expression string
        caller_variables: dict[str, Any] = {}
        try:
            expression_strings = self._inject_nesting(
                {
                    offset: InstructionTranslator(
                        instructions=ops,
                        caller_variables=caller_variables,
                        map_target=self._map_target,
                    ).to_expression(
                        col=col,
                        param_name=self._param_name,
                        depth=int(bool(logical_instructions)),
                    )
                    for offset, ops in control_flow_blocks.items()
                },
                logical_instructions,
            )
        except NotImplementedError:
            return None
        polars_expr = " ".join(expr for _offset, expr in expression_strings)

        # note: if no 'pl.col' in the expression, it likely represents a compound
        # constant value (e.g. `lambda x: CONST + 123`), so we don't want to warn
        if "pl.col(" not in polars_expr:
            return None
        else:
            polars_expr = self._omit_implicit_bool(polars_expr)
            if self._map_target == "series":
                target_name = self._get_target_name(col, polars_expr)
                return polars_expr.replace(f'pl.col("{col}")', target_name)
            else:
                return polars_expr

    def warn(
        self,
        col: str,
        suggestion_override: str | None = None,
        udf_override: str | None = None,
    ) -> None:
        """Generate warning that suggests an equivalent native polars expression."""
        # Import these here so that udfs can be imported without polars installed.

        from polars._utils.various import (
            find_stacklevel,
            in_terminal_that_supports_colour,
        )
        from polars.exceptions import PolarsInefficientMapWarning

        suggested_expression = suggestion_override or self.to_expression(col)

        if suggested_expression is not None:
            target_name = self._get_target_name(col, suggested_expression)
            func_name = udf_override or self._function.__name__ or "..."
            if func_name == "<lambda>":
                func_name = f"lambda {self._param_name}: ..."

            addendum = (
                'Note: in list.eval context, pl.col("") should be written as pl.element()'
                if 'pl.col("")' in suggested_expression
                else ""
            )
            if self._map_target == "expr":
                apitype = "expressions"
                clsname = "Expr"
            else:
                apitype = "series"
                clsname = "Series"

            before, after = (
                (
                    f"  \033[31m- {target_name}.map_elements({func_name})\033[0m\n",
                    f"  \033[32m+ {suggested_expression}\033[0m\n{addendum}",
                )
                if in_terminal_that_supports_colour()
                else (
                    f"  - {target_name}.map_elements({func_name})\n",
                    f"  + {suggested_expression}\n{addendum}",
                )
            )
            warnings.warn(
                f"\n{clsname}.map_elements is significantly slower than the native {apitype} API.\n"
                "Only use if you absolutely CANNOT implement your logic otherwise.\n"
                "Replace this expression...\n"
                f"{before}"
                "with this one instead:\n"
                f"{after}",
                PolarsInefficientMapWarning,
                stacklevel=find_stacklevel(),
            )


class InstructionTranslator:
    """Translates Instruction bytecode to a polars expression string."""

    def __init__(
        self,
        instructions: list[Instruction],
        caller_variables: dict[str, Any],
        map_target: MapTarget,
    ) -> None:
        self._caller_variables: dict[str, Any] = caller_variables
        self._stack = self._to_intermediate_stack(instructions, map_target)

    def to_expression(self, col: str, param_name: str, depth: int) -> str:
        """Convert intermediate stack to polars expression string."""
        return self._expr(self._stack, col, param_name, depth)

    @staticmethod
    def op(inst: Instruction) -> str:
        """Convert bytecode instruction to suitable intermediate op string."""
        if inst.opname in OpNames.CONTROL_FLOW:
            return OpNames.CONTROL_FLOW[inst.opname]
        elif inst.argrepr:
            return inst.argrepr
        elif inst.opname == "IS_OP":
            return "is not" if inst.argval else "is"
        elif inst.opname == "CONTAINS_OP":
            return "not in" if inst.argval else "in"
        elif inst.opname in OpNames.UNARY:
            return OpNames.UNARY[inst.opname]
        elif inst.opname == "BINARY_SUBSCR":
            return "replace"
        else:
            msg = (
                "unrecognized opname"
                "\n\nPlease report a bug to https://github.com/pola-rs/polars/issues"
                " with the content of function you were passing to `map` and the"
                f" following instruction object:\n{inst!r}"
            )
            raise AssertionError(msg)

    def _expr(self, value: StackEntry, col: str, param_name: str, depth: int) -> str:
        """Take stack entry value and convert to polars expression string."""
        if isinstance(value, StackValue):
            op = value.operator
            e1 = self._expr(value.left_operand, col, param_name, depth + 1)
            if value.operator_arity == 1:
                if op not in OpNames.UNARY_VALUES:
                    if e1.startswith("pl.col("):
                        call = "" if op.endswith(")") else "()"
                        return f"{e1}.{op}{call}"
                    if e1[0] in OpNames.UNARY_VALUES and e1[1:].startswith("pl.col("):
                        call = "" if op.endswith(")") else "()"
                        return f"({e1}).{op}{call}"

                    # support use of consts as numpy/builtin params, eg:
                    # "np.sin(3) + np.cos(x)", or "len('const_string') + len(x)"
                    pfx = "np." if op in _NUMPY_FUNCTIONS else ""
                    return f"{pfx}{op}({e1})"
                return f"{op}{e1}"
            else:
                e2 = self._expr(value.right_operand, col, param_name, depth + 1)
                if op in ("is", "is not") and value[2] == "None":
                    not_ = "" if op == "is" else "not_"
                    return f"{e1}.is_{not_}null()"
                elif op in ("in", "not in"):
                    not_ = "" if op == "in" else "~"
                    return (
                        f"{not_}({e1}.is_in({e2}))"
                        if " " in e1
                        else f"{not_}{e1}.is_in({e2})"
                    )
                elif op == "replace":
                    if not self._caller_variables:
                        self._caller_variables.update(_get_all_caller_variables())
                        if not isinstance(self._caller_variables.get(e1, None), dict):
                            msg = "require dict mapping"
                            raise NotImplementedError(msg)
                    return f"{e2}.{op}({e1})"
                elif op == "<<":
                    # Result of 2**e2 might be float is e2 was negative.
                    # But, if e1 << e2 was valid, then e2 must have been positive.
                    # Hence, the output of 2**e2 can be safely cast to Int64, which
                    # may be necessary if chaining operations which assume Int64 output.
                    return f"({e1} * 2**{e2}).cast(pl.Int64)"
                elif op == ">>":
                    # Motivation for the cast is the same as in the '<<' case above.
                    return f"({e1} / 2**{e2}).cast(pl.Int64)"
                else:
                    expr = f"{e1} {op} {e2}"
                    return f"({expr})" if depth else expr

        elif value == param_name:
            return f'pl.col("{col}")'

        return value

    def _to_intermediate_stack(
        self, instructions: list[Instruction], map_target: MapTarget
    ) -> StackEntry:
        """Take postfix bytecode and convert to an intermediate natural-order stack."""
        if map_target in ("expr", "series"):
            stack: list[StackEntry] = []
            for inst in instructions:
                stack.append(
                    inst.argrepr
                    if inst.opname in OpNames.LOAD
                    else (
                        StackValue(
                            operator=self.op(inst),
                            operator_arity=1,
                            left_operand=stack.pop(),  # type: ignore[arg-type]
                            right_operand=None,  # type: ignore[arg-type]
                        )
                        if (
                            inst.opname in OpNames.UNARY
                            or OpNames.SYNTHETIC.get(inst.opname) == 1
                        )
                        else StackValue(
                            operator=self.op(inst),
                            operator_arity=2,
                            left_operand=stack.pop(-2),  # type: ignore[arg-type]
                            right_operand=stack.pop(-1),  # type: ignore[arg-type]
                        )
                    )
                )
            return stack[0]

        # TODO: dataframe.apply(...)
        msg = f"TODO: {map_target!r} apply"
        raise NotImplementedError(msg)


class RewrittenInstructions:
    """
    Standalone class that applies Instruction rewrite/filtering rules.

    This significantly simplifies subsequent parsing by injecting
    synthetic POLARS_EXPRESSION ops into the Instruction stream for
    easy identification/translation and separates the parsing logic
    from the identification of expression translation opportunities.
    """

    _ignored_ops = frozenset(
        [
            "COPY",
            "COPY_FREE_VARS",
            "POP_TOP",
            "PRECALL",
            "PUSH_NULL",
            "RESUME",
            "RETURN_VALUE",
        ]
    )
    _caller_variables: ClassVar[dict[str, Any]] = {}

    def __init__(self, instructions: Iterator[Instruction]):
        self._original_instructions = list(instructions)
        self._rewritten_instructions = self._rewrite(
            self._upgrade_instruction(inst)
            for inst in self._original_instructions
            if inst.opname not in self._ignored_ops
        )

    def __len__(self) -> int:
        return len(self._rewritten_instructions)

    def __iter__(self) -> Iterator[Instruction]:
        return iter(self._rewritten_instructions)

    def __getitem__(self, item: Any) -> Instruction:
        return self._rewritten_instructions[item]

    def _matches(
        self,
        idx: int,
        *,
        opnames: list[AbstractSet[str]],
        argvals: list[AbstractSet[Any] | dict[Any, Any] | None] | None,
        is_attr: bool = False,
    ) -> list[Instruction]:
        """
        Check if a sequence of Instructions matches the specified ops/argvals.

        Parameters
        ----------
        idx
            The index of the first instruction to check.
        opnames
            The full opname sequence that defines a match.
        argvals
            Associated argvals that must also match (in same position as opnames).
        is_attr
            Indicate if the match represents pure attribute access (cannot be called).
        """
        n_required_ops, argvals = len(opnames), argvals or []
        idx_offset = idx + n_required_ops
        if (
            is_attr
            and (trailing_inst := self._instructions[idx_offset : idx_offset + 1])
            and trailing_inst[0].opname in OpNames.CALL  # not pure attr if called
        ):
            return []

        instructions = self._instructions[idx:idx_offset]
        if len(instructions) == n_required_ops and all(
            inst.opname in match_opnames
            and (match_argval is None or inst.argval in match_argval)
            for inst, match_opnames, match_argval in zip_longest(
                instructions, opnames, argvals
            )
        ):
            return instructions
        return []

    def _rewrite(self, instructions: Iterator[Instruction]) -> list[Instruction]:
        """
        Apply rewrite rules, potentially injecting synthetic operations.

        Rules operate on the instruction stream and can examine/modify
        it as needed, pushing updates into "updated_instructions" and
        returning True/False to indicate if any changes were made.
        """
        self._instructions = list(instructions)
        updated_instructions: list[Instruction] = []
        idx = 0
        while idx < len(self._instructions):
            inst, increment = self._instructions[idx], 1
            if inst.opname not in OpNames.LOAD or not any(
                (increment := map_rewrite(idx, updated_instructions))
                for map_rewrite in (
                    # add any other rewrite methods here
                    self._rewrite_functions,
                    self._rewrite_methods,
                    self._rewrite_builtins,
                    self._rewrite_attrs,
                )
            ):
                updated_instructions.append(inst)
            idx += increment or 1
        return updated_instructions

    def _rewrite_attrs(self, idx: int, updated_instructions: list[Instruction]) -> int:
        """Replace python attribute lookup with synthetic POLARS_EXPRESSION op."""
        if matching_instructions := self._matches(
            idx,
            opnames=[{"LOAD_FAST"}, {"LOAD_ATTR"}],
            argvals=[None, _PYTHON_ATTRS_MAP],
            is_attr=True,
        ):
            inst = matching_instructions[1]
            expr_name = _PYTHON_ATTRS_MAP[inst.argval]
            px = inst._replace(
                opname="POLARS_EXPRESSION", argval=expr_name, argrepr=expr_name
            )
            updated_instructions.extend([matching_instructions[0], px])

        return len(matching_instructions)

    def _rewrite_builtins(
        self, idx: int, updated_instructions: list[Instruction]
    ) -> int:
        """Replace builtin function calls with a synthetic POLARS_EXPRESSION op."""
        if matching_instructions := self._matches(
            idx,
            opnames=[{"LOAD_GLOBAL"}, {"LOAD_FAST", "LOAD_CONST"}, OpNames.CALL],
            argvals=[_PYTHON_BUILTINS],
        ):
            inst1, inst2 = matching_instructions[:2]
            if (argval := inst1.argval) in _PYTHON_CASTS_MAP:
                dtype = _PYTHON_CASTS_MAP[argval]
                argval = f"cast(pl.{dtype})"

            px = inst1._replace(
                opname="POLARS_EXPRESSION",
                argval=argval,
                argrepr=argval,
                offset=inst2.offset,
            )
            # POLARS_EXPRESSION is mapped as a unary op, so switch instruction order
            operand = inst2._replace(offset=inst1.offset)
            updated_instructions.extend((operand, px))

        return len(matching_instructions)

    def _rewrite_functions(
        self, idx: int, updated_instructions: list[Instruction]
    ) -> int:
        """Replace function calls with a synthetic POLARS_EXPRESSION op."""
        for function_kind in _MODULE_FUNCTIONS:
            opnames: list[AbstractSet[str]] = [
                {"LOAD_GLOBAL", "LOAD_DEREF"},
                *function_kind["module_opname"],
                *function_kind["attribute_opname"],
                *function_kind["argument_1_opname"],
                *function_kind["argument_1_unary_opname"],
                *function_kind["argument_2_opname"],
                OpNames.CALL,
            ]
            if matching_instructions := self._matches(
                idx,
                opnames=opnames,
                argvals=[
                    *function_kind["module_name"],
                    *function_kind["attribute_name"],
                    *function_kind["function_name"],
                ],
            ):
                attribute_count = len(function_kind["attribute_name"])
                inst1, inst2, inst3 = matching_instructions[
                    attribute_count : 3 + attribute_count
                ]
                if inst1.argval == "json":
                    expr_name = "str.json_decode"
                elif inst1.argval == "datetime":
                    fmt = matching_instructions[attribute_count + 3].argval
                    expr_name = f'str.to_datetime(format="{fmt}")'
                    if not self._is_stdlib_datetime(
                        inst1.argval,
                        matching_instructions[0].argval,
                        fmt,
                        attribute_count,
                    ):
                        return 0
                else:
                    expr_name = inst2.argval

                px = inst1._replace(
                    opname="POLARS_EXPRESSION",
                    argval=expr_name,
                    argrepr=expr_name,
                    offset=inst3.offset,
                )

                # POLARS_EXPRESSION is mapped as a unary op, so switch instruction order
                operand = inst3._replace(offset=inst1.offset)
                updated_instructions.extend(
                    (
                        operand,
                        matching_instructions[3 + attribute_count],
                        px,
                    )
                    if function_kind["argument_1_unary_opname"]
                    else (operand, px)
                )
                return len(matching_instructions)

        return 0

    def _rewrite_methods(
        self, idx: int, updated_instructions: list[Instruction]
    ) -> int:
        """Replace python method calls with synthetic POLARS_EXPRESSION op."""
        LOAD_METHOD = OpNames.LOAD_ATTR if _MIN_PY312 else {"LOAD_METHOD"}
        if matching_instructions := (
            # method call with one basic arg, eg: "s.endswith('!')"
            self._matches(
                idx,
                opnames=[LOAD_METHOD, {"LOAD_CONST"}, OpNames.CALL],
                argvals=[_PYTHON_METHODS_MAP],
            )
            or
            # method call with no arg, eg: "s.lower()"
            self._matches(
                idx,
                opnames=[LOAD_METHOD, OpNames.CALL],
                argvals=[_PYTHON_METHODS_MAP],
            )
        ):
            inst = matching_instructions[0]
            expr = _PYTHON_METHODS_MAP[inst.argval]

            if matching_instructions[1].opname == "LOAD_CONST":
                param_value = matching_instructions[1].argval
                if isinstance(param_value, tuple) and expr in (
                    "str.starts_with",
                    "str.ends_with",
                ):
                    starts, ends = ("^", "") if "starts" in expr else ("", "$")
                    rx = "|".join(re_escape(v) for v in param_value)
                    q = '"' if "'" in param_value else "'"
                    expr = f"str.contains(r{q}{starts}({rx}){ends}{q})"
                else:
                    expr += f"({param_value!r})"

            px = inst._replace(opname="POLARS_EXPRESSION", argval=expr, argrepr=expr)
            updated_instructions.append(px)

        return len(matching_instructions)

    @staticmethod
    def _upgrade_instruction(inst: Instruction) -> Instruction:
        """Rewrite any older binary opcodes using py 3.11 'BINARY_OP' instead."""
        if not _MIN_PY311 and inst.opname in OpNames.BINARY:
            inst = inst._replace(
                argrepr=OpNames.BINARY[inst.opname],
                opname="BINARY_OP",
            )
        return inst

    def _is_stdlib_datetime(
        self, function_name: str, module_name: str, fmt: str, attribute_count: int
    ) -> bool:
        if not self._caller_variables:
            self._caller_variables.update(_get_all_caller_variables())
        vars = self._caller_variables
        return (
            attribute_count == 0 and vars.get(function_name) is datetime.datetime
        ) or (attribute_count == 1 and vars.get(module_name) is datetime)


def _is_raw_function(function: Callable[[Any], Any]) -> tuple[str, str]:
    """Identify translatable calls that aren't wrapped inside a lambda/function."""
    try:
        func_module = function.__class__.__module__
        func_name = function.__name__
    except AttributeError:
        return "", ""

    # numpy function calls
    if func_module == "numpy" and func_name in _NUMPY_FUNCTIONS:
        return "np", f"{func_name}()"

    # python function calls
    elif func_module == "builtins":
        if func_name in _PYTHON_CASTS_MAP:
            return "builtins", f"cast(pl.{_PYTHON_CASTS_MAP[func_name]})"
        elif func_name == "loads":
            import json  # double-check since it is referenced via 'builtins'

            if function is json.loads:
                return "json", "str.json_decode()"

    return "", ""


def warn_on_inefficient_map(
    function: Callable[[Any], Any], columns: list[str], map_target: MapTarget
) -> None:
    """
    Generate `PolarsInefficientMapWarning` on poor usage of a `map` function.

    Parameters
    ----------
    function
        The function passed to `map`.
    columns
        The column names of the original object; in the case of an `Expr` this
        will be a list of length 1 containing the expression's root name.
    map_target
        The target of the `map` call. One of `"expr"`, `"frame"`,
        or `"series"`.
    """
    if map_target == "frame":
        msg = "TODO: 'frame' map-function parsing"
        raise NotImplementedError(msg)

    # note: we only consider simple functions with a single col/param
    if not (col := columns and columns[0]):
        return None

    # the parser introspects function bytecode to determine if we can
    # rewrite as a much more optimal native polars expression instead
    parser = BytecodeParser(function, map_target)
    if parser.can_attempt_rewrite():
        parser.warn(col)
    else:
        # handle bare numpy/json functions
        module, suggestion = _is_raw_function(function)
        if module and suggestion:
            fn = function.__name__
            parser.warn(
                col,
                suggestion_override=f'pl.col("{col}").{suggestion}',
                udf_override=fn if module == "builtins" else f"{module}.{fn}",
            )


__all__ = ["BytecodeParser", "warn_on_inefficient_map"]
