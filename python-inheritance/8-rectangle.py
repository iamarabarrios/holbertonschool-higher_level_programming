#!/usr/bin/python3
"""Defines a class Rectangle that inherits from BaseGeometry."""


BaseGeometry = __import__("7-base_geometry").BaseGeometry

class Rectangle(BaseGeometry):
    """Represent the rectangle using base geometry."""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        slef.__width = width
        self.integer_validator("height", height)
        self.__height = height
