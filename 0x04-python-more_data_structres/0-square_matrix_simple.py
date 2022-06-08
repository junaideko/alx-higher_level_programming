#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    newMatrix1 = []
    for i in matrix:
        newMatrix = list(map(lambda x: x ** 2, i))
        newMatrix1.append(newMatrix)
    return newMatrix1
