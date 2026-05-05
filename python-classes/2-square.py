#!/usr/bin/python3
"""This module defines a Square class with private size attribute."""


class Square:
    """This class represents a square with a private size attribute."""

    def __init__(self, size=0):
        """Initialize a new Square instance with size validation.

        Args:
            size (int): The size of the square. Defaults to 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
