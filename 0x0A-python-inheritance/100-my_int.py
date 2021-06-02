#!/usr/bin/python3
""" This program defines a class MyInt """


class MyInt(int):
    """ This class inherits from the class int """
    def __eq__(self, x: object):
        return super().__eq__(not x)

    def __ne__(self, x: object):
        return super().__ne__(not x)
