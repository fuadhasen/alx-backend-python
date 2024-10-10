#!/usr/bin/env python3
"""module for complex type: function"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a function that multiplies a float by a given multiplier."""
    def multiply_by_multiplier(value: float) -> float:
        return value * multiplier
    return multiply_by_multiplier
