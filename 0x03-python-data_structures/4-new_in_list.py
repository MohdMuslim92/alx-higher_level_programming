#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    length = len(my_list)
    list_copy = my_list.copy()
    if idx < 0 or idx >= length:
        return my_list
    else:
        list_copy[idx] = element
        return list_copy
