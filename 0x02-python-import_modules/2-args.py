#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = sys.argv[1:]
    count = len(args)
    i = 1
    if len(args) > 0:
        arguments = "argument" if count == 1 else "arguments"
        print("{} {}:".format(count, arguments))
        for arg in args:
            print("{}: {}".format(i, arg))
            i = i + 1
    else:
        print("0 arguments.")
