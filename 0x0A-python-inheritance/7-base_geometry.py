#!/usr/bin/python3

"""This module defines a class BaseGeometry with public
instance method area and integer_validator."""


class BaseGeometry(object):
    """Class BaseGeometry with public instance method area
    and integer_validator that validates value: if value is
    not an integer: raise a TypeError exception, if value is
    less or equal to 0: raise a ValueError exception."""

    def __init__(self):
        pass

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
