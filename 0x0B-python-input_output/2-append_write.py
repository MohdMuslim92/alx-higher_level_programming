#!/usr/bin/python3

"""This module is about appending a string at the end of a text file
(UTF8) and returns the number of characters added"""


def append_write(filename="", text=""):
    """Function that appends a string at the end of a text file
    encoded with (UTF8) and returns the number of characters added
    using with statement"""
    with open(filename, "a", encoding="UTF8") as my_file:
        my_file.write(text)
        return len(text)
