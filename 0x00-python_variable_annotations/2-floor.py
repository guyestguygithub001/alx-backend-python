#!/usr/bin/env python3
"""
A module for demonstrating variable annotations by computing the floor of a float.
"""

import math

def floor(n: float) -> int:
    """
    Return the floor of a float number.

    Args:
        n (float): The float number to compute the floor of.

    Returns:
        int: The floor of `n`.
    """
    return math.floor(n)
