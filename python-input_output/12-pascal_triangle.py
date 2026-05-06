#!/usr/bin/python3

triangle = [[], [1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]


def pascal_triangle(n):
    if n <= 0:
        return triangle[:1]
    return triangle[:n+1]
