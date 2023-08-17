#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    def squared(x):
        return x ** 2

    result_matrix = [[squared(value) for value in row] for row in matrix]

    return result_matrix
