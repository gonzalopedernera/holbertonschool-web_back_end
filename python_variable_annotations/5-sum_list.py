#!/usr/bin/env python3
"""
Type-annotated function 'sum_list'
Takes a list of floats as argument and returns their sum as a float.
"""


def sum_list(input_list: list) -> float:
    """Sums all the values of a list returning a float"""
    return sum(val for val in input_list)
