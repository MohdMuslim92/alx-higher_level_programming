#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    length = len(my_list)
    divisible_list = []
    for i in range(length):
        if my_list[i] % 2 == 0:
            divisible_list.append(True)
        else:
            divisible_list.append(False)
    return divisible_list
