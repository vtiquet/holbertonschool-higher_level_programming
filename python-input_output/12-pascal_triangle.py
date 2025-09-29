#!/usr/bin/python3
"""Function that returns a list of lists of integers
representing the Pascal’s triangle of n."""


def pascal_triangle(n):
    """
    Returns a list of lists of integers
    representing the Pascal’s triangle of n.
    Returns an empty list if n <= 0.
    """
    if n <= 0:
        return []

    else:
        triangle = []
        for i in range(n):
            row = [1]
            if i > 0:
                prev_row = triangle[i - 1]
                for j in range(len(prev_row) - 1):
                    row.append(prev_row[j] + prev_row[j + 1])
                row.append(1)
            triangle.append(row)
        return triangle
