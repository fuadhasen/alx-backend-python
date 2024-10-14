#!/usr/bin/env python3
"""scripts for basics of async"""
import random


async def wait_random(max_delay: int = 10) -> float:
    """asyncronus function"""
    wait_time = random.uniform(0, max_delay)
    return wait_time
