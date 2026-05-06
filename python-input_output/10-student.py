#!/usr/bin/python3
"""
Module that defines a Student class.
"""


class Student:
    """
    Represents a student with first name, last name, and age.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a new Student instance.

        Args:
            first_name (str): The student's first name.
            last_name (str): The student's last name.
            age (int): The student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns a dictionary representation of the Student instance.

        If attrs is a list of strings,
        only attribute names contained in this list is retrieved..

        Args:
            attrs (list, optional): List of attribute names to retrieve.
                                    Defaults to None.

        Returns:
            dict: A dictionary of the requested attributes.
        """
        if (
            isinstance(attrs, list) and
            all(isinstance(item, str) for item in attrs)
        ):
            return {key: getattr(self, key)
                    for key in attrs
                    if hasattr(self, key)}
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'age': self.age
        }
