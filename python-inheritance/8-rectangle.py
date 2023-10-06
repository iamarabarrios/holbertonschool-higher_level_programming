#!/usr/bin/python3
"""Defines a class Rectangle that inherits from BaseGeometry."""


class Rectangle(BaseGeometry):
    """Represent the rectangle using base geometry."""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        slef.__width = width
        self.integer_validator("height", height)
        self.__height = height
