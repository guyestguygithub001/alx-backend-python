#!/usr/bin/env python3
"""
A module for demonstrating variable annotations by summing a mixed list of integers and floats.
"""

from typing import List, Union

def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Sum a mixed list of integers and float numbers and return the sum as a float.

    Args:
        mxd_lst (List[Union[int, float]]): The mixed list of integers and float numbers to sum.

    Returns:
        float: The sum of all numbers in `mxd_lst`.
    """
    return float(sum(mxd_lst))
