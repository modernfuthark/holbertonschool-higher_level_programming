#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = []
    for i in range(0, len(matrix)):
        new.append(list(map(lambda x: x ** 2, matrix[i])))
    return (new)
