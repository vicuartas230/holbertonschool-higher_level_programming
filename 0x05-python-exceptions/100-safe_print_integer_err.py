#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except ValueError as v_error:
        print("Exception: {}".format(v_error), file=sys.stderr)
        return False
    except TypeError as t_error:
        print("Exception: {}".format(t_error), file=sys.stderr)
        return False
