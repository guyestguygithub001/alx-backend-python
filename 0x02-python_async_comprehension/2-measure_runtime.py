#!/usr/bin/env python3
"""
Task 2: Run time for four parallel comprehensions

This script measures the execution time of running four asynchronous comprehensions in parallel.
"""

import asyncio
import time
from 1-async_comprehension import async_comprehension

async def measure_runtime() -> float:
    """
    Measures the runtime of executing async_comprehension concurrently four times.

    This function records the start time, concurrently runs four instances of async_comprehension,
    waits for all to complete, and then calculates the total time taken for execution.

    Returns:
        float: The total time elapsed, in seconds, for the concurrent execution.
    """
    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time.time() - start_time
