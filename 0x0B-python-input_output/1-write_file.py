#!/usr/bin/python3
""" This program defines a function write_file """


def write_file(filename="", text=""):
    """ This function writes a string to a text file (UTF8)
        and returns the number of characters written """
    with open(filename, 'w') as new:
        writting = new.write(text)
    new.close()
    return writting
