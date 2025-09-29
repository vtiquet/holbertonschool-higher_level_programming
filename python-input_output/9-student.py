#!/usr/bin/python3
"""Class Student that defines a student."""


class Student:
    """Defines a student with first_name, last_name, and age."""
    def __init__(self, first_name, last_name, age):
        """Initialize a new Student instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieve a dictionary representation of a Student instance."""
        pass

