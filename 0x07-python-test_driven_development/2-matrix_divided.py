#!/usr/bin/python3
"""matrix_divided"""
from email import message
from operator import is_not


def matrix_divided(matrix, div):
    """divide a matrix by a given number"""
    message = "matrix must be a matrix (list of lists) of integers/floats"
    res_matrix = []
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")

    for lists in matrix:
        if len(lists) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        otherlist = []
        for items in lists:
            if not isinstance(items, (int, float)):
                raise TypeError(message)
            else:
                otherlist.append(round(items / div, 2))
        res_matrix.append(otherlist)

    return res_matrix
