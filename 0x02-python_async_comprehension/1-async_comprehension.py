#!/usr/bin/env python3
"""scripts for Async comprehensions"""
import asyncio
import random
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List:
    """async comprehesion function"""
    res = [i async for i in async_generator()]
    return res
