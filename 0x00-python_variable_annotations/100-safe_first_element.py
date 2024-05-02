#!/usr/bin/env python3
"""
Task 10: Duck Typing - First Element of a Sequence

This module demonstrates duck typing by attempting to retrieve the first element of any sequence.
"""

from typing import Any, Sequence, Union

def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Attempt to return the first element of a sequence.

    This function checks if the sequence 'lst' is not empty and returns the first element.
    If the sequence is empty, it returns None.

    Args:
        lst: A sequence from which the first element is to be retrieved.

    Returns:
        The first element of the sequence if it exists, otherwise None.
    """
    if lst:
        return lst[0]
    else:
        return None
