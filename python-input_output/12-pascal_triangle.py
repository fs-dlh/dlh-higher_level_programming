#!/usr/bin/python3
"""
Module that defines a Pascal's Triangle class.
"""


triangle = [[], [1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]


def pascal_triangle(n):
    """
    Initializes a new Student instance.

    Args:
        n (int): Number of rows to generate.

    Returns:
        list: A list of lists representing the Pascal's Triangle.
    """

    if n <= 0:
        return triangle[:1]
    return triangle[:n+1]
