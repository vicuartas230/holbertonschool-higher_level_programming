#!/usr/bin/python3
""" This program defines a function to check
    if an object is an instance of a class """
def is_kind_of_class(obj, a_class):
    """ This function returns True if the object
        is an instance of, or if the object is an
        instance of a class that inherited from,
        the specified class ; otherwise False """
    if isinstance(obj, a_class):
        return True
    else:
        return False
