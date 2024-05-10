#!/usr/bin/env python3
"""
Module for Task 2 - Measure the runtime
"""
import asyncio
import time
from typing import List

# Assuming async_comprehension is defined in the module named '1-async_comprehension'
from 1-async_comprehension import async_comprehension

async def measure_runtime() -> float:
    """
    Coroutine will execute async_comprehension four times in parallel using asyncio.gather.
    measure_runtime should measure the total runtime and return it.
    """
    start_time = time.time()
    tasks = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*tasks)
    end_time = time.time()
    return end_time - start_time

async def main():
    """
    Main function to print the return value of measure_runtime
    """
    print(await measure_runtime())

# Running the main function
asyncio.run(main())
