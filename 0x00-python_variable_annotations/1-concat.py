#!/usr/bin/env python3
"""
A module to demonstrate variable annotations by concatenating strings.
"""

def concat(str1: str, str2: str) -> str:
    """
    Concatenate two strings and return the result.

    Args:
        str1 (str): The first string to concatenate.
        str2 (str): The second string to concatenate.

    Returns:
        str: The concatenated string of `str1` and `str2`.
    """
    return str1 + str2
