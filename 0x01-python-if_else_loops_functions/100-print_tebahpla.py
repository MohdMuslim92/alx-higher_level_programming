#!/usr/bin/python3
flag = 0
minus = 0
for i in range(122, 96, -1):
    if flag == 0:
        flag = 1
        minus = 0
    else:
        flag = 0
        minus = 32
    print("{}".format(chr(i - minus)), end="")
