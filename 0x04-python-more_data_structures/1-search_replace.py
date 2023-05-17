#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    i = 0
    for element in my_list:
        if element == search:
            new_list.append(replace)
            i += 1
            continue
        new_list.append(my_list[i])
        i += 1
    return new_list
