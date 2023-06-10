#!/usr/bin/python3

"""This module creates addition function.
:param a: The first integer or float.
:param b: The second integer or float. Defaults to 98.
:raises TypeError: If `a` or 'b' is not an integer or float
:return: The addition of `a` and `b` as an integer."""


def add_integer(a, b=98):
    """Function that adds two numbers.
    :raises TypeError: if 'a' or 'b' is not an integer or float
    :return: The addition of `a` and `b` as an integer."""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
        if isinstance(b, float):
            b = int(b)
    return a + b
