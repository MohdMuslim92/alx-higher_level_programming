#!/usr/bin/python3
def uniq_add(my_list=[]):
    my_list.sort()
    filtered_list = my_list
    i = 0
    result = 0
    for element in my_list:
        if my_list[i] == my_list[i + 1]:
            filtered_list.pop(i)
            i += 1
    for item in filtered_list:
        result += item
    return result
