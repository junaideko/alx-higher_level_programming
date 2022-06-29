#!/usr/bin/python3
"""module provides 2-matrix_divided function tht divids
all element of a matrix"""


def matrix_divided(matrix, div):
    """method divide each element of a mtrix by div
        Args:
            matrix(list): of int and floats
            div(int): a number int or float
        Returns: a new matrix
    """
    if not isinstance(matrix, list):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/f;oats")
        sizeOf1stRow = None
        if sizeOf1stRow is None:
            sizeOf1stRow = len(row)
        elif sizeOf1stRow != len(row):
            raise TypeError("Each row of the matrix must have the same size")
        for item in row:
            if not isinstance(item, (int, float)):
                raise TypeError(
                  "matrix must be a matrix (list of lists) of integers/floats")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(item / div, 2) for item in row] for row in matrix]
