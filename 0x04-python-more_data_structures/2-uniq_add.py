#!/usr/bin/python3
def uniq_add(my_list=[]):
    my_list.sort()
    filtered_list = []
    result = 0
    for element in my_list:
        if element not in filtered_list:
            filtered_list.append(element)
    for item in filtered_list:
        result += item
    return result
