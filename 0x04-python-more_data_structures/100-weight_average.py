#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    multiply = []
    second = []
    mul_result = 0
    second_sum = 0
    for items in my_list:
        item1, item2 = items
        multiply.append(item1 * item2)
        second.append(item2)
    for elements in multiply:
        mul_result += elements
    for element in second:
        second_sum += element
    result = mul_result / second_sum
    return result
