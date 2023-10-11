#!/usr/bin/python3
"""Write the class Rectangle that inherits from Base."""


from .base import Base


class Rectangle(Base):
    """This is the rectangle class."""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new instance of the rectangle class."""
        super().__init__(id)

        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if not isinstance(y, int):
            raise TypeError("y must be an integer")

        if width <= 0:
            raise ValueError("width must be > 0")
        if height <= 0:
            raise ValueError("height must be > 0")
        if x < 0:
            raise ValueError("x must be >= 0")
        if y < 0:
            raise ValueError("y must be >= 0")

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """Sets the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width and validates the types and values."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height and validates the types and values."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Get the coordinate x."""
        return self.__x

    @x.setter
    def x(self, value):
        """Validate types and values."""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Get the coordinate y."""
        return self.__y

    @y.setter
    def y(self, value):
        """Validate types and values."""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Return the area rectangle."""
        return self.__width * self.__height

    def display(self):
        """Improve the print the rectangle in stdout using #."""
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """Actualize the class rectangle."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)

    def update(self, *args):
        """Asigment attributes."""
        attributes = ["id", "width", "height", "x", "y"]

        if args:
            for i in range(len(args)):
                if i < len(attributes):
                    setattr(self, attributes[i], args[i])
        else kwargs:
            for key, value in kwargs.items():
                if key in attributes:
                    setattr(self, key, value)
