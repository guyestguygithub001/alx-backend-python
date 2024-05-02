#!/usr/bin/env python3
"""
Task 12: Type Checking

This module demonstrates creating multiple copies of items in a tuple by zooming in.
"""

from typing import List, Tuple

def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Creates multiple copies of items in a tuple.

    Args:
        lst (Tuple): The input tuple containing items.
        factor (int, optional): The zoom factor (number of copies). Defaults to 2.

    Returns:
        List: A list containing the zoomed-in items.
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in

array = (12, 72, 91)

zoom_2x = zoom_array(array)  # Zoomed in 2x

zoom_3x = zoom_array(array, 3)  # Zoomed in 3x
