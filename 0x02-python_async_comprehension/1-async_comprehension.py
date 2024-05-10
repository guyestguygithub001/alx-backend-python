#!/usr/bin/env python3
"""
Task 1: Async Comprehensions

This script demonstrates the use of asynchronous comprehensions to generate a list of random numbers.
The async_comprehension coroutine will asynchronously gather 10 random numbers produced by the async_generator function.
"""

import typing
from 0-async_generator import async_generator

async def async_comprehension() -> typing.List[float]:
    """
    Asynchronously generates a list of 10 random numbers.

    This coroutine utilizes an asynchronous comprehension to iterate over the async_generator function,
    which yields 10 random numbers, and collects them into a list.

    Returns:
        typing.List[float]: A list containing 10 randomly generated numbers.
    """
    return [rand async for rand in async_generator()]
