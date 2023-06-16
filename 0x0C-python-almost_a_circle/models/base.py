#!/usr/bin/python3
import json

"""This module defines a class Base"""


class Base:
    """
    Base class.

    Attributes:
        __nb_objects (int): Private class attribute to keep track
        of the number of objects created.
        id (int): Public instance attribute representing the unique
        identifier for each object.
        If id is provided, assign it to the id attribute.
        Otherwise, increment __nb_objects and assign the new value
        to the id attribute.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize the Base object.

        Args:
        id (int, optional): Unique identifier for the object.
        Defaults to None.
            If provided, it will be assigned to the id attribute.
            If not provided, __nb_objects will be incremented, and
            its value will be assigned to the id attribute.
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Return the JSON string representation of list_dictionaries.

        Args:
            list_dictionaries (list): List of dictionaries.

        Returns:
            str: JSON string representation of list_dictionaries.
        """

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)
