#!/usr/bin/env python3
"""scripts for asyncio.Task."""
import asyncio
from asyncio import Task

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Task[float]:
    """asyncio Task"""
    task = asyncio.create_task(wait_random(max_delay))
    return task
