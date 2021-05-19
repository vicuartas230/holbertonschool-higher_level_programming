#!/usr/bin/python3
import math
""" This program defines a class MagicClass """


class MagicClass:
    """ Class to return the circumference area """
    def __init__(self, radius=0):
        if type(radius) is not int or type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        return (self.radius ** 2) * math.pi

    def circumference(self):
        return 2 * math.pi * self.__radius
