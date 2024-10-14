#!/usr/bin/env python3
"""scripts for multiple coroutines at the same time with  async"""
import asyncio
import random
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """multiple corroutines at same time"""
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    delays = []

    for task in asyncio.as_completed(tasks):
        res = await task
        delays.append(res)

    return delays
