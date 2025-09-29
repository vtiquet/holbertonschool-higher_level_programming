#!/usr/bin/python3
"""Class Student that defines a student with JSON filtering capabilities."""


class Student:
    """Defines a student with first_name, last_name, and age."""
    def __init__(self, first_name, last_name, age):
        """Initialize a new Student instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieve a dictionary representation of a Student instance.
        If attrs is a list of strings, only attributes contained in this list must be retrieved.
        """
        pass

