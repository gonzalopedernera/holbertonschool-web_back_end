#!/usr/bin/env python3
"""
Type-annotated function to_kv
Takes a string k and an int OR float v as arguments and returns a tuple.
The first element of the tuple is the string k.
The second element is the square of the int/float v
It should be annotated as a float.
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Returns a tuple(k, v ** 2)"""
    return k, v ** 2
