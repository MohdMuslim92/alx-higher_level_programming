#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        return fct(*args)
    except Exception as ex_type:
        print("Exception: {}".format(ex_type), file=sys.stderr)
        return None
