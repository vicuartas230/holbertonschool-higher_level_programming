#!/usr/bin/python3
""" This program defines a function append_write """


def append_write(filename="", text=""):
    """ This function appends a string at the end of a text
        file (UTF8) and returns the number of characters added """
    with open(filename, 'a') as new:
        appended = new.write(text)
    new.close()
    return appended
