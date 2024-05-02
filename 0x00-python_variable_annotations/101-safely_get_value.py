#!/usr/bin/env python3
"""
Task 11: More Involved Type Annotations

This module demonstrates advanced type annotations by defining a function that attempts to retrieve a value from a dictionary.
"""

from typing import Any, Mapping, Union, TypeVar

# TypeVar allows for specifying type parameters in generic types.
T = TypeVar('T')
# Res can be any type or a specific type T.
Res = Union[Any, T]
# Def can be type T or None.
Def = Union[T, None]

def safely_get_value(dct: Mapping, key: Any, default: Def = None) -> Res:
    """
    Attempt to retrieve a value from a dictionary using a specified key.

    This function checks if the key is present in the dictionary 'dct' and returns the associated value.
    If the key is not found, it returns the 'default' value.

    Args:
        dct: A dictionary from which to retrieve the value.
        key: The key to look up in the dictionary.
        default: The default value to return if the key is not found.

    Returns:
        The value associated with 'key' in 'dct' if it exists, otherwise 'default'.
    """
    if key in dct:
        return dct[key]
    else:
        return default
