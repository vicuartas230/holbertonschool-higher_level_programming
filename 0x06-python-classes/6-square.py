#!/usr/bin/python3
""" This program defines a class Square. """


class Square:
    """ A class to represent a Square. """
    def __init__(self, size=0, position=(0, 0)):
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        if len(position) != 2 or type(position[0]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if position[0] < 0 or position[1] < 0 or type(position[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if len(value) != 2 or type(value[0]) != int or type(value[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if x[0] < 0 or x[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """ Function that returns the area of a square """
        x = self.__size
        return x * x

    def my_print(self):
        """ Function that prints a square of characters # """
        length = self.__size
        if not length:
            print('')
        for m in range(self.__position[1]):
            print('')
        for i in range(length):
            for k in range(self.__position[0]):
                print(' ', end='')
            for j in range(length):
                print('#', end='')
            print('')
