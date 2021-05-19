#!/usr/bin/python3
""" This program defines a class Square. """


class Square:
    """ A class to represent a Square. """
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        x = self.__size
        return x * x
