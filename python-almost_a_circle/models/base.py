#!/usr/bin/python3
"""Write the first class Base."""


import jason


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the json string representation of diciotnary list."""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)
