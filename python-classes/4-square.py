#!/usr/bin/python3
"""This module defines a Square class with size validation and area method."""


class Square:
    """This class represents a square with a private size attribute."""

    def __init__(self, size=0):
        """Initialize a new Square instance with size validation.

        Args:
            size (int): The size of the square. Defaults to 0.
        """
        self.size = size  # Uses the setter for validation

    @property
    def size(self):
        """Retrieve the size of the square.

        Returns:
            int: The current size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with validation.

        Args:
            value (int): The new size value.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate and return the area of the square.

        Returns:
            int: The area of the square (size multiplied by size).
        """
        return self.__size * self.__size
