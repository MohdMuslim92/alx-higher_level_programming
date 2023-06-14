#!/usr/bin/python3

"""This module adds all arguments to a Python list, and then save
them to a file"""


import sys
import json


def save_to_json_file(my_obj, filename):
    """Function that writes an object to a text file using
    a JSON representation.

    Args:
        my_obj: The object to save as JSON.
        filename (str): The name of the file to save.

    Returns:
        None
    """
    with open(filename, 'w') as file:
        json.dump(my_obj, file)


def load_from_json_file(filename):
    """Function that creates an object from a JSON file.

    Args:
        filename (str): The name of the JSON file.

    Returns:
        object: The Python object represented by the JSON file.
    """
    with open(filename, 'r') as file:
        my_obj = json.load(file)
        return my_obj


try:
    existing_data = load_from_json_file('add_item.json')
except FileNotFoundError:
    existing_data = []

arguments = sys.argv[1:]
existing_data.extend(arguments)

save_to_json_file(existing_data, 'add_item.json')
