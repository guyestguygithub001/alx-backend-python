#!/usr/bin/env python3
"""
Task 1: Concurrent Execution with Asyncio
This task focuses on running multiple asynchronous coroutines concurrently
using the async/await syntax.
"""

import asyncio
from typing import List

# Importing the wait_random function from the 1st task
wait_random = __import__("0-basic_async_syntax").wait_random

async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Execute multiple coroutines concurrently and return the delays.

    This function runs 'n' number of 'wait_random' coroutines concurrently and
    returns a list of the delays (as float values) experienced by each coroutine,
    sorted in ascending order.
    """
    waits = await asyncio.gather(
        *list(map(lambda _: wait_random(max_delay), range(n)))
    )

    return sorted(waits)
