#!/usr/bin/python3
"""Define a class Square with private instance attributes size, validation, area method, size property, my_print method, and comparators."""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initialize a new square.

        Args:
            size (int): The size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value (int): The new size of the square.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Compute the area of the square."""
        return self.__size ** 2

    def __eq__(self, other):
        """Check if two squares are equal."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Check if two squares are not equal."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Check if one square is smaller than the other."""
        return self.area() < other.area()

    def __le__(self, other):
        """Check if one square is smaller than or equal to the other."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Check if one square is greater than the other."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Check if one square is greater than or equal to the other."""
        return self.area() >= other.area()
