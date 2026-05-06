#!/usr/bin/python3
"""
Module for reading and printing the contents of a UTF-8 text file.
"""


def read_file(filename=""):
    """
    Reads a UTF-8 text file and prints its content to stdout.

    Args:
        filename (str): The name of the file to read. Defaults to empty string.

    Returns:
        None

    Example:
        >>> read_file("example.txt")
        Hello, World!
    """
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            print(line, end='')
