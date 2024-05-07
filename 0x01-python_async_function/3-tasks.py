#!/usr/bin/env python3
"""
Task 3: Asynchronous Task Creation
This script demonstrates how to create an asynchronous task using the asyncio library.
"""

import asyncio

# Importing the wait_random function from the first task
wait_random = __import__('0-basic_async_syntax').wait_random

def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Generate an asyncio.Task that runs the wait_random coroutine.

    This function creates an asyncio.Task object that will execute the wait_random coroutine,
    which waits for a random delay up to 'max_delay' seconds before completing.
    """
    return asyncio.create_task(wait_random(max_delay))
