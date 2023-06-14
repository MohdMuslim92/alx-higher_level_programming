#!/usr/bin/python3

"""This module returns the dictionary description with simple
data structure (list, dictionary, string, integer and boolean)
for JSON serialization of an object"""


def class_to_json(obj):
    """Function that returns the dictionary description with simple data structure
    (list, dictionary, string, integer, and boolean) for JSON serialization of an object.

    Args:
        obj: An instance of a class.

    Returns:
        dict: The dictionary representation of the object for JSON serialization.
    """
    attributes = vars(obj)
    json_dict = {}

    for attr, value in attributes.items():
        if isinstance(value, (list, dict, str, int, bool)):
            json_dict[attr] = value

    return json_dict

