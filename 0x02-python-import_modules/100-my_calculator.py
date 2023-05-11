#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    args = sys.argv[0:]
    count = len(args)

    if count != 4:
        print("Usage: {} <a> <operator> <b>".format(args[0]))
        exit(1)
    a = int(args[1])
    operator = args[2]
    b = int(args[3])

    addition = add(a, b)
    subtraction = sub(a, b)
    multiplication = mul(a, b)
    division = div(a, b)
    if operator == '+':
        print("{} + {} = {}".format(a, b, addition))
    elif operator == '-':
        print("{} - {} = {}".format(a, b, subtraction))
    elif operator == '*':
        print("{} * {} = {}".format(a, b, multiplication))
    elif operator == '/':
        print("{} / {} = {}".format(a, b, division))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
