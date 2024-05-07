#!/usr/bin/env python3
"""
Task 4: Asynchronous Task Execution
This module focuses on executing the 'task_wait_random' coroutine multiple times.
"""

import asyncio
from typing import List

# Importing the task_wait_random function from the previous module
task_wait_random = __import__('3-tasks').task_wait_random

async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Execute the 'task_wait_random' coroutine 'n' times concurrently.

    This function creates 'n' instances of the 'task_wait_random' coroutine and
    gathers their results. It returns a sorted list of the delays (as float values)
    experienced by each coroutine.
    """
    wait_times = await asyncio.gather(
        *tuple(map(lambda _: task_wait_random(max_delay), range(n)))
    )
    return sorted(wait_times)
