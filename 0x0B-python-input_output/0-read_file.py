#!/usr/bin/python3

"""This module is about reading a text file unicoded with
(UTF8) and prints it to stdout"""


def read_file(filename=""):
    """Function that reads a text file (UTF8) and prints it to stdout:
    using with statement"""
    with open(filename, encoding="UTF8") as my_file:
        while True:
            lines = my_file.read(4096).rstrip()
            if not lines:
                break
            if lines:
                print(lines)
