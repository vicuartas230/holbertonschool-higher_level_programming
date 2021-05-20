#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        return fct(*args)
    except ZeroDivisionError as Z_err:
        print("Exception: {}".format(Z_err), file=sys.stderr)
    except IndexError as idx_err:
        print("Exception: {}".format(idx_err), file=sys.stderr)
