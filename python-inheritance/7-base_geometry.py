#!/usr/bin/python3
"""Write a class BaseGeometry."""


class BaseGeometry:
    """Represent base geometry."""
    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value < 0 or value == 0:
            raise ValueError("{} must be greater than 0".format(name))
