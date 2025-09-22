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
        if type(value) is bool:
            raise TypeError(f"{name} must be an integer")
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
