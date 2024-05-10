#!/usr/bin/env python3
"""
Module for Task 1 - Async Comprehension
"""
import asyncio
from typing import List

# Assuming async_generator is defined in the module named '0-async_generator'
from 0-async_generator import async_generator

async def async_comprehension() -> List[float]:
    """
    Coroutine will collect 10 random numbers using an async comprehensing over async_generator, then return the 10 random numbers.
    """
    return [i async for i in async_generator()]

async def main():
    """
    Main function to print the return value of async_comprehension
    """
    print(await async_comprehension())

# Running the main function
asyncio.run(main())
