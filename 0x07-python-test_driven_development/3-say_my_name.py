#!/usr/bin/python3
""" This program is used to test all posible
    special cases in the function say_my_name """


def say_my_name(first_name, last_name=""):
    """ This function prints My name is <first name> <last name>
        first_name is a string to print instead of <first_name>
        last_name is a string to print instead of <last_name> """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
