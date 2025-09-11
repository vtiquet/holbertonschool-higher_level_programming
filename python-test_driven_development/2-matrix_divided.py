#!/usr/bin/python3
"""
This module contains the function matrix_divided
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix.

    Args:
        matrix (list of lists): The matrix to divide.
        div (int or float): The number to divide by.

    Returns:
        list of lists: A new matrix with divided elements.

    Raises:
        TypeError: If matrix is not a list of lists of ints/floats,
                   or if rows have different sizes, or if div is not a number.
        ZeroDivisionError: If div is 0.
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if not isinstance(matrix, list) or \
       not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix"
                        "(list of lists) of integers/floats")

    if not matrix or not matrix[0]:
        return []

    row_length = len(matrix[0])
    new_matrix = []

    for row in matrix:
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")

        new_row = []
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("matrix must be a matrix"
                                "(list of lists) of integers/floats")
            new_row.append(round(element / div, 2))
        new_matrix.append(new_row)

    return new_matrix
