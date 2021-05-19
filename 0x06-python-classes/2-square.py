#!/usr/bin/python3
""" This program defines a class Square. """


class Square:
    """ A class to represent a Square. """
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
