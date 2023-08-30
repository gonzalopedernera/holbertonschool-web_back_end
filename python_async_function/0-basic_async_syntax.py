#!/usr/bin/env python3
"""
Asynchronous coroutine named wait_random
Takes in an integer argument (max_delay, with a default value of 10)
Waits for a random delay between 0 and max_delay seconds
Eventually returns it.
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Waits for a random delay between 0 and max_delay seconds
    Eventually returns it.
    """
    random_float = random.uniform(0, max_delay)
    await asyncio.sleep(random_float)
    return random_float
