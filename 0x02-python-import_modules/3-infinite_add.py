#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = sys.argv[1:]
    count = len(args)
    result = 0
    if len(args) > 0:
        for arg in args:
            result += int(arg)
        print("{}".format(result))
    else:
        print("0")
