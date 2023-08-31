#!/usr/bin/env python3
"""
Async routine called wait_n
Takes in 2 int arguments (in this order): n and max_delay.
It will spawn wait_random n times with the specified max_delay.
"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Spawn wait_random n times with the specified max_delay."""
    spawns = []
    for i in range(n):
        spawns.append(await task_wait_random(max_delay))
    return sorted(spawns)
