#!/usr/bin/python3

"""This module creates a class Student that defines a student
and retrieves a dictionary representation of a Student instance"""


class Student:
    """Class that defines a student."""

    def __init__(self, first_name, last_name, age):
        """Instantiation with first_name, last_name, and age.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves a dictionary representation of a Student instance.

        Returns:
            dict: The dictionary representation of the Student instance.
        """
        attributes = vars(self)
        json_dict = {}

        for attr, value in attributes.items():
            if isinstance(value, (list, dict, str, int, bool)):
                json_dict[attr] = value

        return json_dict
