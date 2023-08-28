#!/usr/bin/env python3
"""
Type-annotated function 'make_multiplier'.
Takes a float 'multiplier' as argument.
Returns a function that multiplies a float by 'multiplier'.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a function that multiplies 'multiplier' by a float"""
    def mul_by_mul(num: float) -> float:
        """Returns the result of 'multiplier' * float"""
        return multiplier * num
    return mul_by_mul
