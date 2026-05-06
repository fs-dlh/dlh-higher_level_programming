#!/usr/bin/python3
"""
Module for writing a string to a UTF-8 text file.
"""


def append_write(filename="", text=""):
    """
    Writes a string to a text file (UTF-8)
    and returns the number of characters written.

    Args:
        filename (str): The name of the file to write to.
                        Defaults to empty string.
        text (str): The string to write into the file.
                        Defaults to empty string.

    Returns:
        int: Number of characters written.
    """
    with open(filename, 'a', encoding='utf-8') as file:
        num_chars = file.write(text)
    return num_chars
