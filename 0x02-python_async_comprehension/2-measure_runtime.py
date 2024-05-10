#!/usr/bin/env python3
'''Creates Run time for different four parallel comprehensions
'''

import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''Executes an async_comprehension 4 times, measures
    total run time
    '''
    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time.time() - start_time
