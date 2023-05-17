#!/usr/bin/python3
from functools import reduce


def uniq_add(my_list=[]):
    my_list.sort()
    filtered_list = my_list
    i = 0
    for element in my_list:
        if my_list[i] == my_list[i + 1]:
            filtered_list.pop(i)
            i += 1
    result = reduce((lambda x, y: x + y), filtered_list)
    return result
