#!/usr/bin/python3
"""This module creates a function that prints a text with 2
new lines after each of these characters: ., ? and :"""


def text_indentation(text):
    """Function that prints a newline after every ., ? and :"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    flag = 0
    for c in text:
        if c == "." or c == "?" or c == ":":
            print(c, end="")
            print("\n")
            flag = 1
            continue
        if flag == 1 and c == " ":
            flag = 0
            continue
        print(c, end="")
