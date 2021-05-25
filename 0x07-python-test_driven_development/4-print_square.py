#!/usr/bin/python3
""" This program is used to test all posible special cases
    in the function print_square """


def print_square(size):
    """ This function prints a square with the character #
        size is the lenght of width
        and the height """
    if size < 0 and type(size) == float:
        raise TypeError("size must be an integer")
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for rows in range(size):
        print('#' * size)
