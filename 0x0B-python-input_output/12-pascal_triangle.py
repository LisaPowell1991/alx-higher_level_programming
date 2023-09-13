#!/usr/bin/python3

""" A module that contains a function, pascal_triangle """


def pascal_triangle(n):
    """
    A list of lists of integers representing
    the Pascal’s triangle of n.

    Args:
    @n (int): Integer that is going to be use

    Returns:
    a list of lists of integers representing
    the Pascal’s triangle of n;
    or empty list if n <= 0
    """

    if n <= 0:
        return []

    triangle = []
    for row_index in range(n):
        row = []
        for column_index in range(row_index + 1):
            if column_index == 0 or column_index == row_index:
                row.append(1)
            else:
                prev_row = triangle[row_index - 1]
                value = prev_row[column_index - 1] + prev_row[column_index]
                row.append(value)
        triangle.append(row)

    return triangle               
