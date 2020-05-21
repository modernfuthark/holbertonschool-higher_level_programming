#!/usr/bin/python3
""" 2-matrix_divided: Divides a matrix """


def matrix_divided(matrix, div):
    """ matrix_divided: Divide the matrix 'matrix' by 'div' """

    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists) \
of integers/floats")
    for i in matrix:
        if type(i) is not list:
            raise TypeError("matrix must be a matrix (list of lists) \
of integers/floats")
        for j in i:
            if type(j) not in [int, float]:
                raise TypeError("matrix must be a matrix (list of lists) \
of integers/floats")
    for i in matrix:
        if len(i) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new = [[round(j / div, 2) for j in i] for i in matrix]
    return new
