#!/usr/bin/env python3
"""
The below function’s parameters and return values with the appropriate types

def element_length(lst):
    return [(i, len(i)) for i in lst]
"""
from typing import Sequence, Tuple, List, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Function with correct types for parameters and return"""
    return [(i, len(i)) for i in lst]
