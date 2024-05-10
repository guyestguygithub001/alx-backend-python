#!/usr/bin/env python3
'''Async Comprehensions
Imports async_generator from task 0 and then write
a coroutine called async_comprehension that takes null arguments

coroutine collects 10 different numbers using an async
comprehensing over async_generator, returns the 10 random
numbers
'''

import typing

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> typing.List[float]:
    '''Makes list of 10 numbers from given 10-number generator
    '''
    return [rand async for rand in async_generator()]
