#!/usr/bin/python3
def remove_char_at(str, n):
    characters = ''
    string = list(str)
    if n < len(string) and n >= 0:
        string.pop(n)
    for letters in string:
        characters += letters
    return characters
