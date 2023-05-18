#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    remove_keys = []
    for keys, values in a_dictionary.items():
        if values == value:
            remove_keys.append(keys)
    for key in remove_keys:
        a_dictionary.pop(key, None)
    return a_dictionary
