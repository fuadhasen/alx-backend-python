#!/usr/bin/env python3
"""scripts for Async comprehensions"""
import time
from typing import List

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """measure runtime function"""
    start = time.time()
    await async_comprehension()
    end = time.time()

    total = end - start
    return total
