#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        result = fct(*args)
    except (RuntimeError, IndexError, ZeroDivisionError) as err:
        print("Exception: {}".format(err), file=sys.stderr)
        result = None
    return (result)
