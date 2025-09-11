#!/usr/bin/python3
"""
This module contains the function say_my_name, which prints a name.
"""


def say_my_name(first_name, last_name=""):
    """
    Prints a name in the format "My name is <first name> <last name>".

    Args:
        first_name (str): The first name.
        last_name (str): The last name, defaults to an empty string.

    Returns:
        None.

    Raises:
        TypeError: If first_name or last_name is not a string.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
