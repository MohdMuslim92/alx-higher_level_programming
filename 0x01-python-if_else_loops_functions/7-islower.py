#!/usr/bin/python3
def islower(c):
    char_code = ord(c)
    if char_code >= 97 and char_code <= 122:
        return True
    else:
        return False
