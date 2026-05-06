#!/usr/bin/python3
"""
Module that defines a Pascal's Triangle class.
"""


triangle = [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]


def pascal_triangle(n):
    """
    Initializes a new Student instance.

    Args:
        n (int): Number of rows to generate.

    Returns:
        list: A list of lists representing the Pascal's Triangle.
    """

    if n <= 0:
        return triangle[:0]

    for row in range(5, n):
        new_row = [1]
        for i in range(1, row):
            new_row.append(triangle[row - 1][i - 1] + triangle[row - 1][i])
        new_row.append(1)
        triangle.append(new_row)

    return triangle[:n]
