#!/usr/bin/env python3
"""module for complext type: string and int/float to tuple"""
from typing import List, Union, Tuple


def to_kv(k: str, v: Union[float, int]) -> Tuple[str, float]:
    """function that compute problem"""

    return (k, float(v * v))
