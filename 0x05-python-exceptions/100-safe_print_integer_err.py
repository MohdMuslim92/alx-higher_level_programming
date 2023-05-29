#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except Exception as ex_type:
        print("Exception: {}".format(ex_type), file=sys.stderr)
        return False
    return True
