#!/usr/bin/python3

"""This module defines a class MyList that inherits list."""


class MyList(list):
    """This class is inherits list"""

    def print_sorted(self):
        """Function that prints a sorted list"""

        sorted_list = sorted(self)
        print(sorted_list)
