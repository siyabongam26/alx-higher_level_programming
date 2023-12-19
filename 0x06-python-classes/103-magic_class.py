#!/usr/bin/python3
"""Define a class MagicClass that mimics the provided Python bytecode."""


import math


class MagicClass:
    """Represent a magic class."""

    def __init__(self, radius=0):
        """Initialize a new magic class.

        Args:
            radius: The radius of the magic class.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Compute the area of the magic class."""
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        """Compute the circumference of the magic class."""
        return 2 * math.pi * self.__radius
