#!/usr/bin/python3
"""
This module demonstrates multiple inheritance with the FlyingFish class.
"""


class Fish():
    def swim(self):
        print("The fish is swimming")

    def habitat(self):
        print("The fish live in water")


class Bird():
    def fly(self):
        print("The bird is flying")

    def habitat(self):
        print("The bird lives in the sky")


class FlyingFish():
    def fly(self):
        print("The flying fish is soaring!")

    def swim(self):
        print("The flying fish is swimming!")

    def habitat(self):
        print("The flying fish lives both in water and the sky!")
