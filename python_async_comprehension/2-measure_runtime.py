#!/usr/bin/env python3
"""
Execute async_comprehension four times in parallel using asyncio.gather.
Measures the total runtime and returns it
"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Returns the total runtime of async_comprehension.
    """
    start = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for i in range(4)))
    end = time.perf_counter()
    return end - start
