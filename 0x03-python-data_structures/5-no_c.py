#!/usr/bin/python3
def no_c(my_string):
    string_copy = []
    for char in my_string:
        if char.lower() != 'c' or char.upper() != 'C':
            string_copy.append(char)
    new_string = ''.join(string_copy)
    return new_string
