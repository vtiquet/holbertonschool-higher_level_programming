#!/usr/bin/python3
"""
This module defines the MyList class.
"""


class MyList(list):
    """
    A class MyList that inherits from list, with a method to print sorted.
    """
    def print_sorted(self):
        print(sorted(self))
