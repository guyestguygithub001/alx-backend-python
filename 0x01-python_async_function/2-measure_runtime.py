#!/usr/bin/env python3
"""
Task 2: Runtime Analysis
This script is designed to measure and analyze the runtime of asynchronous operations.
"""

import asyncio
import time

# Importing the wait_n function from the previous task
wait_n = __import__('1-concurrent_coroutines').wait_n

def measure_time(n: int, max_delay: int) -> float:
    """
    Calculate the average time taken for 'n' asynchronous operations.

    This function measures the total time taken to execute 'n' instances of the 'wait_n' coroutine
    with a maximum delay of 'max_delay' seconds. It then computes and returns the average time per operation.
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    elapsed_time = time.time() - start_time
    average_time = elapsed_time / n
    return average_time
