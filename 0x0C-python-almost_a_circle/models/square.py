#!/usr/bin/python3
from models.rectangle import Rectangle

"""
This module defines the Square class, a subclass of the Base class.

The Square class represents a square shape and inherits common
attributes and methods from the Base class.
It provides additional attributes and methods specific to squares,
such as side length and area calculation.

Classes:
    Square: Represents a square shape and inherits from the Base class.

Module Functions:
    None

Exceptions:
    None

"""


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
        return "[Square] ({}) {}/{} - {}".format(
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

    def update(self, *args, **kwargs):
        """
        Assign attributes based on no-keyworded and key-worded arguments.

        Args:
            *args: No-keyworded arguments representing the id, size,x,
            and y attributes.
            **kwargs: Key-worded arguments representing the attributes
            to be updated.

        Note:
            If *args exists and is not empty, **kwargs will be skipped.
        """

        if len(args) > 0:
            self.id = args[0]
        if len(args) > 1:
            self.size = args[1]
        if len(args) > 2:
            self.x = args[2]
        if len(args) > 3:
            self.y = args[3]

        if args:
            return

        for key, value in kwargs.items():
            if key == 'id':
                self.id = value
            elif key == 'size':
                self.size = value
            elif key == 'x':
                self.x = value
            elif key == 'y':
                self.y = value

    def to_dictionary(self):
        """
        Return the dictionary representation of the square.

        Returns:
            dict: Dictionary containing the attributes of the square.
        """
        return {
                'id': self.id,
                'size': self.width,
                'x': self.x,
                'y': self.y
                }

    def to_csv_row(self):
        """Return a list representing a single row in the CSV file."""
        return [self.id, self.size, self.x, self.y]
