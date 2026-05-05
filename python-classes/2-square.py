#!/usr/bin/python3
""" This module defines a Square class with private size attribute. """


class Square:
    """ This class represents an Square class with private size attribute. It validates the size attribute """

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
