#!/usr/bin/env python3
"""scripts for  Async Generator"""
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """async generator function"""
    for _ in range(10):
        await asyncio.sleep(1)
        wait_time = random.uniform(0, 10)
        yield wait_time
