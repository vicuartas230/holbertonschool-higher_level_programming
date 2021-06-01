#!/usr/bin/python3
""" This program defines a function lookup """


def lookup(obj):
    """ This function returns the list of available
        attributes and methods of an object """
    return obj.__dict__
