#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    length = len(my_list)
    if idx < 0 or idx >= length:
        return my_list
    else:
        remove = my_list[idx]
        my_list.remove(remove)
        return my_list
