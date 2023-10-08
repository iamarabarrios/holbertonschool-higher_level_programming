#!/usr/bin/python3
"""Define rectangle subclass square."""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent a square."""
    def __init__(self, size):
        """Initialize new square."""
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Return the description of square."""
        return "[Square] {}/{}".format(self.__size, self.__size)
