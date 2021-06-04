#!/usr/bin/python3
""" This program defines a function pascal_triangle """


def pascal_triangle(n):
    """ This function returns a list of lists of integers
        representing the Pascal’s triangle of n """
    lines = []
    for row in range(1, (n + 1)):
        elemts = []
        item = 1
        for column in range(1, (row + 1)):
            elemts.append(item)
            item = round(item * (row - column) / column)
        lines.append(elemts)
    return lines
