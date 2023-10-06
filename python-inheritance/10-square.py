#!/usr/bin/python3
"""Write a class Square that inherits from Rectangle (9-rectangle.py):"""


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Represent a square."""
    def __init__(self, size):
        """Represent new square."""
        super().integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Area"""
        return self.__size ** 2
