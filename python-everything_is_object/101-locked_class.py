#!/usr/bin/python3
"""
A class that uses __slots__ to prevent the user from dynamically creating
new instance attributes, except if the new instance attribute is called
'first_name'. This reduces memory cost by avoiding the instance dictionary.
"""


class LockedClass:
    __slots__ = ['first_name']
