#!/usr/bin/env python3
'''
Task 2: Run time for four parallel comprehensions
This script measures the execution time for running the async_comprehension coroutine four times in parallel.
'''

import asyncio
import time

# Importing the async_comprehension function from the '1-async_comprehension' module
async_comprehension = __import__('1-async_comprehension').async_comprehension

async def measure_runtime() -> float:
    '''
    Executes the async_comprehension coroutine four times concurrently and measures the total execution time.
    '''
    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time.time() - start_time
