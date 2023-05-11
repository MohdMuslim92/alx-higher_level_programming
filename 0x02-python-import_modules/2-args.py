#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = sys.argv[1:]
    i = 1
    arguments = "arguments" if len(args) > 1 else "argument"
    if len(args) > 0:
        print("{} {}:".format(len(args), arguments))
        for arg in args:
            print("{}: {}".format(i, sys.argv[i]))
            i = i + 1
        else:
            print("0 arguments.")
