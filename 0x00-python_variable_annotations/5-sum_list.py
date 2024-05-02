#!/usr/bin/env python3
"""
A module for demonstrating variable annotations by summing a list of floats.
"""

from typing import List

def sum_list(input_list: List[float]) -> float:
    """
    Sum a list of float numbers and return the sum.

    Args:
        input_list (List[float]): The list of float numbers to sum.

    Returns:
        float: The sum of all float numbers in `input_list`.
    """
    return sum(input_list)
