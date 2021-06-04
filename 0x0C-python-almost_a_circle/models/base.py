#!/usr/bin/python3
""" This program defines a class Base """


class base:
    """ This class will be the “base” of all other classes in this project. """
    __nb_objects = 0
    def __init__(self, id=None):
        if id:
            self.id = id
        else:
            self.__nb_objects += 1
            self.id = self.__nb_objects
