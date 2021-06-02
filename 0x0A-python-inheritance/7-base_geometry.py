#!/usr/bin/python3
""" This program defines a class BaseGeometry """


class BaseGeometry:
    """ This class defines the attributes to handle the geometry
        in some subclasses """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        self.name = name
        self.value = value
