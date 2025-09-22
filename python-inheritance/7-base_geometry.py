#!/usr/bin/python3
"""
This module defines the BaseGeometry class
with an area method and integer_validator.
"""


class BaseGeometry:
    """
    A class BaseGeometry with an unimplemented
    area method and an integer_validator.
    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")
