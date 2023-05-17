#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    set_1 = list(set_1)
    set_2 = list(set_2)
    first_list = set_1
    for element in set_2:
        if element not in first_list:
            first_list.append(element)
        else:
            first_list.remove(element)
    return first_list
