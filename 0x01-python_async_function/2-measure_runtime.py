#!/usr/bin/env python3
"""scripts for Measuring the runtime"""
import time
import asyncio
from typing import List

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """measure run time or wait_n function"""
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()

    total = end - start
    return total / n
