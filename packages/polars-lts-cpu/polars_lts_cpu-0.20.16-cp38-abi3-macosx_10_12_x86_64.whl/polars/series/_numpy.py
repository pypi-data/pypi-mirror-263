from __future__ import annotations

import ctypes
from typing import Any

import numpy as np


# https://numpy.org/doc/stable/user/basics.subclassing.html#slightly-more-realistic-example-attribute-added-to-existing-array
class SeriesView(np.ndarray):  # type: ignore[type-arg]
    def __new__(
        cls, input_array: np.ndarray[Any, Any], owned_object: Any
    ) -> SeriesView:
        # Input array is an already formed ndarray instance
        # We first cast to be our class type
        obj = input_array.view(cls)
        # add the new attribute to the created instance
        obj.owned_series = owned_object
        # Finally, we must return the newly created object:
        return obj

    def __array_finalize__(self, obj: Any) -> None:
        # see InfoArray.__array_finalize__ for comments
        if obj is None:
            return
        self.owned_series = getattr(obj, "owned_series", None)


# https://stackoverflow.com/questions/4355524/getting-data-from-ctypes-array-into-numpy
def _ptr_to_numpy(
    ptr: int, shape: int | tuple[int, int] | tuple[int], ptr_type: Any
) -> np.ndarray[Any, Any]:
    """
    Create a memory block view as a numpy array.

    Parameters
    ----------
    ptr
        C/Rust ptr casted to usize.
    shape
        Shape of the array values.
    ptr_type
        Example:
            f32: ctypes.c_float)

    Returns
    -------
    numpy.ndarray
        View of memory block as numpy array.
    """
    ptr_ctype = ctypes.cast(ptr, ctypes.POINTER(ptr_type))
    if isinstance(shape, int):
        shape = (shape,)
    return np.ctypeslib.as_array(ptr_ctype, shape)
