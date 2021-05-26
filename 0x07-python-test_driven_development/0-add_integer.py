#!/usr/bin/python3
""" This program is used to test all posible
    special cases of the function add_integter """


def add_integer(a, b=98):
    """ This function returns the add of two integers
        a is the first number to add
        b is the second number to add """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b
