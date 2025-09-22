#!/usr/bin/python3
"""
This module defines the inherits_from function.
"""


def inherits_from(obj, a_class):
    """
    Checks if an object is an instance of a class
    that inherited (directly or indirectly)
    from the specified class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if obj's class inherited from a_class, False otherwise.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
