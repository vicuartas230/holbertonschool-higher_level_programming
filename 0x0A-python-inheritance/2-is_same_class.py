#!/usr/bin/python3
""" This program defines a function is_same_class
    to check if an object is an instance of a
    class """


def is_same_class(obj, a_class):
    """ This function returns True if the object
        is exactly an instance of the specified
        class ; otherwise False. """
    if type(obj) is a_class:
        return True
