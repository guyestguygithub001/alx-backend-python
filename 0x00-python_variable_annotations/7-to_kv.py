#!/usr/bin/env python3
from typing import Union, Tuple

def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple with the first element as the string 'k' and the second element as the square of 'v'.
    The second element is annotated as a float.
    """
    return k, v ** 2.0

# Example usage
print(to_kv("eggs", 3))  # ('eggs', 9.0)
print(to_kv("school", 0.02))  # ('school', 0.0004)
