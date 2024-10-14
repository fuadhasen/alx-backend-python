#!/usr/bin/env python3
"""scripts for basics of async"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """asyncronus function"""
    wait_time = random.uniform(0, max_delay)
    await asyncio.sleep(wait_time)
    return wait_time
