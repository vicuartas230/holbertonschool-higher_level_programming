#!/usr/bin/python3
""" This program defines a class MyList """


class MyList(list):
    """ This class inherits from class list """
    def print_sorted(self):
        s = sorted(self)
        print(s)
