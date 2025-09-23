#!/usr/bin/python3
"""
This module demonstrates how to use mixins to compose class behaviors.
"""


class SwimMixin():
    def swim(self):
        print("The creature swims!")


class FlyMixin():
    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    def roar(self):
        print("The dragon roars!")
