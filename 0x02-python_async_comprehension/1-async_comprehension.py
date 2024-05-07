#!/usr/bin/env python3
'''
Task 1: Async Comprehensions
This script demonstrates the use of async comprehensions to collect a list of random numbers.
It imports the async_generator coroutine from the previous task.
'''

import typing

# Importing the async_generator function from the '0-async_generator' module
async_generator = __import__('0-async_generator').async_generator

async def async_comprehension() -> typing.List[float]:
    '''
    Asynchronously collects 10 random numbers generated by the async_generator.
    It uses an async comprehension to create a list of these numbers and returns it.
    '''
    return [rand async for rand in async_generator()]
