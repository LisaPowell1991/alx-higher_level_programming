#!/usr/bin/python3

""" Module that contains a class, matrix_divided """


def matrix_divided(matrix, div):
    """
    This class that represents a function
    that divides all elements of a matrix.

    args:
    param matrix: list of lists of integers or floats
    div: The number oto divide all elements
    of the matrix by(can't be 0)

    Raises:
    TypeError: If matrix is not a list of lists of integer/float
               if each row of the matrix doesn't have the same size
               or if div is not a number(int or float)
    ZeroDivisionError: If div = 0
    """
    err_msg = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list) or not all(
            isinstance(row, list) and all(
                isinstance(x, (int, float)) for x in row
                ) for row in matrix
            ):
        raise TypeError(err_msg)

    if not matrix:
        raise TypeError(err_msg)

    row_size = len(matrix[0])
    if not all(len(row) == row_size for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(num / div, 2) for num in row] for row in matrix]

    return new_matrix
