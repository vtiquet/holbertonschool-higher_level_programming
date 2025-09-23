#!/usr/bin/python3
"""
This module defines classes for shapes and a function to calculate their
area and perimeter using duck typing.
"""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return abs(math.pi * self.radius ** 2)

    def perimeter(self):
        return abs(2 * math.pi * self.radius)


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


def shape_info(object):
    print(f"Area: {object.area()}")
    print(f"Perimeter: {object.perimeter()}")
