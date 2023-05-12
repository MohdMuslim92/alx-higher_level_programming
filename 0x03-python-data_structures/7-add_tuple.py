#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    list_result = []
    tuple_list_a = list(tuple_a)
    tuple_list_b = list(tuple_b)
    if len(tuple_list_a) < 2:
        tuple_list_a.extend([0] * (2 - len(tuple_list_a)))
    if len(tuple_list_b) < 2:
        tuple_list_b.extend([0] * (2 - len(tuple_list_b)))
    a = tuple_list_a[0] + tuple_list_b[0]
    b = tuple_list_a[1] + tuple_list_b[1]
    list_result.append(a)
    list_result.append(b)
    tuple_result = tuple(list_result)
    return tuple_result
