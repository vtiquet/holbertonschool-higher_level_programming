#!/usr/bin/python3
"""
This module contains the function print_square, which prints a square.
"""


def print_square(size):
    """
    Prints a square with the # character.

    Args:
        size (int): The size length of the square.

    Returns:
        None.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.
    """
    if not isinstance(size, int):
        if isinstance(size, float) and size < 0:
            raise TypeError("size must be an integer")
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size == 0:
        print("")
        return

    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
