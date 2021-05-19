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

    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def position(self):
        return self.position

    @position.setter
    def position(self, value):
        x = self.__position
        if len(x) != 2 or type(x[0]) != int or type(x[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        x = self.__size
        return x * x

    def my_print(self):
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
