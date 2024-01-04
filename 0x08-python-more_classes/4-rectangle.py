#!/usr/bin/python3
"""Module for defining the Rectangle class"""


class Rectangle:
    """Class representing a rectangle"""

    def __init__(self, width=0, height=0):
        """Initialization method with optional width and height"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter method for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method for width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter method for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method for height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Method to calculate and return the rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """Method to calculate and return the rectangle perimeter"""
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Method to create a string representation of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ""
        return '\n'.join(['#' * self.__width for _ in range(self.__height)])

    def __repr__(self):
        """Method to create a representation of the rectangle"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Method to print a message when an instance is deleted"""
        print("Bye rectangle...")

if __name__ == "__main__":
    # Test cases
    my_rectangle = Rectangle(2, 4)
    print(str(my_rectangle))
    print("--")
    print(my_rectangle)
    print("--")
    print(repr(my_rectangle))
    print("--")
    print(hex(id(my_rectangle)))
    print("--")

    # create a new instance based on representation
    new_rectangle = eval(repr(my_rectangle))
    print(str(new_rectangle))
    print("--")
    print(new_rectangle)
    print("--")
    print(repr(new_rectangle))
    print("--")
    print(hex(id(new_rectangle)))
    print("--")

    print(new_rectangle is my_rectangle)
    print(type(new_rectangle) is type(my_rectangle))
