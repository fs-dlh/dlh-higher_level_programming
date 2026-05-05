#!/usr/bin/python3
"""This module defines a Square class with size validation and area method."""


class Square:
    """This class represents a square with a private size attribute and area."""

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

    def area(self):
        """Calculate and return the area of the square.

        Returns:
            int: The area of the square (size multiplied by size).
        """
        return self.__size * self.__size

