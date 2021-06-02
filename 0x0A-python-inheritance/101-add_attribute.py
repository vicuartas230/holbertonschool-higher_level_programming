#!/usr/bin/python3
""" This program defines a function add_attribute """


def add_attribute(_class, name, value):
    """ This function adds a new attribute to an object if it’s possible """
    if type(_class) is str or type(_class) is int:
        raise TypeError("can't add new attribute")
    setattr(_class, name, value)
