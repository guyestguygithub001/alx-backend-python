#!/usr/bin/env python3
"""
Task 0: Understanding Asynchronous Operations
Create an asynchronous coroutine named `wait_random` that accepts an integer
parameter (`max_delay`, defaulting to 10). This coroutine should wait for a
random duration between 0 and `max_delay` seconds (inclusive, with a floating-point
value) before returning the elapsed time.

This task requires the use of the `random` module.
"""

import asyncio
import random

async def wait_random(max_delay: int = 10) -> float:
    """
    Pause execution for a random duration.
    
    This coroutine pauses for a random duration that's less than or equal to `max_delay` seconds,
    then returns the actual time waited.
    """
    wait_seconds: float = random.uniform(0, max_delay)
    await asyncio.sleep(wait_seconds)
    return wait_seconds
