#!/usr/bin/python3
"""
Module that provides a function
to convert a class instance to a JSON-serializable dictionary.
"""


def class_to_json(obj):
    """
    Returns a dictionary description of an object for JSON serialization.

    Args:
        obj: An instance of a class.

    Returns:
        dict: A dictionary containing all serializable attributes of the
              object, where keys are attribute names and values are the
              attribute values that are of type list, dict, str, int, or bool.
    """
    result = {}
    for key, value in obj.__dict__.items():
        # Check if the value is one of the JSON-serializable types
        if type(value) in (list, dict, str, int, bool):
            result[key] = value
    return result
