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
