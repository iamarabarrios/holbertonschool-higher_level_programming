#!/usr/bin/python3
"""Write a class Square that defines a square."""


class Square:
    """Represent a square."""
    def __init__(self, size=0):
        """Initialize a new sqaure."""
        self.size = size

    @property
    def size(self):
        """Get the size of square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of square."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Calculate the area of square."""
        return self.__size ** 2
