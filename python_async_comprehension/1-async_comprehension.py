#!/usr/bin/env python3
"""
Collects 10 random numbers using an async comprehensing over async_generator.
Then return the 10 random numbers.
"""
import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Collects 10 random numbers using async_generator.
    Then returns them.
    """
    return [i async for i in async_generator()]
