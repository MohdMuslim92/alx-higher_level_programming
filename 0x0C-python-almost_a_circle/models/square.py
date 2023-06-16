#!/usr/bin/python3
from models.rectangle import Rectangle

"""This module defines a class Square that inherits from Rectangle"""


class Square(Rectangle):
    """
    Square class that inherits from the Rectangle class.

    Attributes:
        size (int): Size of the square.
        x (int): X-coordinate of the square's position.
        y (int): Y-coordinate of the square's position.
        id (int): Unique identifier for the square.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize the Square object.

        Args:
            size (int): Size of the square.
            [optional] x (int): X-coordinate of the square's position.
            Defaults to 0.
            [optional] y (int): Y-coordinate of the square's position.
            Defaults to 0.
            [optional] id (int): Unique identifier for the square.
            Defaults to None.

        Note:
            The id, x, y, width, and height arguments are passed to
            the super class constructor (Rectangle) using the super()
            function. The width and height are assigned the value of
            size.
        """

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return a string representation of the square."""
        return "[square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """Get the size of the square."""
        return self.width

    @size.setter
    def size(self, value):
        """Set the size of the square."""
        self.width = value
        self.height = value
