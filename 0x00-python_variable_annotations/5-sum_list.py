#!/usr/bin/env python3
"""module for complex types: list of list"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """function that compute problem"""
    sum = 0
    for i in input_list:
        sum += i

    return sum
