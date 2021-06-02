#!/usr/bin/python3
""" This program defines a function add_attribute """


def add_attribute(_class, name, value):
    """ This function adds a new attribute to an object if it’s possible """
    if not hasattr(_class, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(_class, name, value)
