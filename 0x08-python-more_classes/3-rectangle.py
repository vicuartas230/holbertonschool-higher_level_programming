#!/usr/bin/python3
""" This program defines a class Rectangle """


class Rectangle:
    """ Define all instances for class Rectangle """
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if not self.__height or not self.__width:
            return 0
        return self.__width * 2 + self.__height * 2

    def __str__(self):
        rectangle = ''
        for row in range(self.__height):
            for column in range(self.__width):
                rectangle += '#'
            if row < self.__height - 1:
                rectangle += '\n'
        return rectangle
