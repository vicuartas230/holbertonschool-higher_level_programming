#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
""" This program defines a class Rectangle """


class Rectangle(BaseGeometry):
    """ This class defines a subclass of the class
        BaseGeometry to use the width and height arguments
        to create a area method """
    def __init__(self, width, height):
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return "[{}] {}/{}\
".format(__class__.__name__, self.__width, self.__height)
