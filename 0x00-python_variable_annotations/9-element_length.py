#!/usr/bin/env python3
from typing import Iterable, Sequence, List, Tuple

def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Calculate the length of each element in the iterable.

    This function takes an iterable containing sequences, and returns a list of tuples.
    Each tuple contains an element from the iterable and the length of that element.

    Args:
        lst: An iterable containing sequences.

    Returns:
        A list of tuples, where each tuple contains a sequence from the iterable and its length.
    """
    return [(i, len(i)) for i in lst]

# The annotations will show up when calling the __annotations__ attribute
print(element_length.__annotations__)
