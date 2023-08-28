#!/usr/bin/env python3
"""
Type-annotated function 'sum_mixed_list'
Takes a list 'mxd_lst' of integers and floats and returns their sum as a float.
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Sums all the values of a list returning a float"""
    return sum(val for val in mxd_lst)
