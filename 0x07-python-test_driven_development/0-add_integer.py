#!/usr/bin/python3
""" This function adds two integers """


def add_integer(a, b=98):
    """ This function returns the add of two integers """
    if type(a) is not [int, float]:
        raise TypeError("a must be an integer")
    if type(b) is not [int, float]:
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b
