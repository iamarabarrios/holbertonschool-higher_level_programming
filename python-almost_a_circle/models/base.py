#!/usr/bin/python3
"""Write the first class Base."""


class Base:
    """This is the base class."""


    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

