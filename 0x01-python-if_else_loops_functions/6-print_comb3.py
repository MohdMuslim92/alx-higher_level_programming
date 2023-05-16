#!/usr/bin/python3
for i in range(9):
    if i != 8:
        separator = ", "
    else:
        separator = ""
    for j in range(10):
        if j > i:
            print("{}{}".format(i, j), end=separator)
print()
