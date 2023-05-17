#!/usr/bin/python3
def common_elements(set_1, set_2):
    set_1 = list(set_1)
    set_2 = list(set_2)
    common = []
    j = 0
    for element1 in set_1:
        for element2 in set_2:
            if element1 == element2:
                common.append(set_1[j])
        j += 1
    return common
