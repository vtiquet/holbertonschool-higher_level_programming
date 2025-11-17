#!/usr/bin/python3
"""
Prevents dynamic creation of new instance attributes,
except if the new instance attribute is called first_name.
"""


class LockedClass:
    __slots__ = ["first_name"]

    def __init__(self):
        """Initialize class instance."""
        pass
