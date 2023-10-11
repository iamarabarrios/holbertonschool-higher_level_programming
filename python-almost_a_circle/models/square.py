#!/usr/bin/python3
"""Square."""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square of rectangle."""
    def __init__(self, size, x=0, y=0, id=None):
        """Constructor of class square."""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Represent the method str, square."""
        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """Getter for the attribute size."""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for the attribute size."""
        self.width = value
        self.height = value
