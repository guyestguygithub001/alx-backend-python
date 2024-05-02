#!/usr/bin/env python3
'''Returns a function tha truns a float
'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''Returns the result by multiplying it by the multiplier
    '''
    return lambda x: x * multiplier
