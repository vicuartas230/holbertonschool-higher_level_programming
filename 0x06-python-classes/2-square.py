#!/usr/bin/python3
""" This program defines a class Square. """
class Square:
    """ A class to represent a Square. """
    def __init__(self, size=0):
        if size < 0:
            raise ValueError
        if type(size) != int:
            raise TypeError
        try:
            self.__size = size
        except TypeError:
            print("size must be an integer")
        except ValueError:
            print("size must be >= 0")
