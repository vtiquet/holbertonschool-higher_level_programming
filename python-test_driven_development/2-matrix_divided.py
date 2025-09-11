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
    if not isinstance(matrix, list) or \
       not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix"
                        "(list of lists) of integers/floats")

    if not all(isinstance(elem, (int, float))
               for row in matrix for elem in row):
        raise TypeError("matrix must be a matrix"
                        "(list of lists) of integers/floats")

    if len(matrix) > 0 and not all(len(row) == len(matrix[0])
                                   for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for row in matrix:
        new_row = [round(elem / div, 2) for elem in row]
        new_matrix.append(new_row)

    return new_matrix
