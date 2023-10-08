#!/usr/bin/python3
"""Write a class Student that defines a student by:"""


class Student:
    """Represent the student."""
    def __init__(self, first_name, last_name, age):
        """Initialize the new student."""
        self.age = age
        self.last_name = last_name
        self.first_name = first_name

    def to_json(self, attrs=None):
        """Get a dictionary representation of the Student."""
        if attrs is None:
            return self.__dict__

        return {
            attr: getattr(self, attr)
            for attr in attrs if hasattr(self, attr)
        }
