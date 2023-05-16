#!/usr/bin/python3
for i in range(100):
    if i != 99:
        separator = ", "
    else:
        separator = ""
    print("{:02d}".format(i), end=separator)
print()
