#!/usr/bin/python3
""" This program is used to test all
    especial cases of a division of
    a matrix for a number div """


def matrix_divided(matrix, div):
    """ This function divides all elements of a matrix
        matrix is the list of lists
        div is the number to divide each element of matrix """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    rows = []
    for row in range(len(matrix)):
        element = []
        for position in matrix[row]:
            if not isinstance(position, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) \
of integers/floats")
            element.append(round(position / div, 2))
        if len(matrix[row]) != len(matrix[0]):
                raise TypeError("Each row of the matrix must \
have the same size")
        rows.append(element)
    return rows
