#!/usr/bin/python3
""" This program defines a class Rectangle """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ This class defines a subclass Square of the subclass
        Rectangle of the class BaseGeometry to use the
        width and height arguments to create a area method """
    def __init__(self, size):
        super().integer_validator("size", size)
        self.__size = size

    def area(self):
        return self.__size * self.__size

    def __str__(self):
        return "[{}] {}/{}\
".format(__class__.__name__, self.__size, self.__size)
