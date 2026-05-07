#!/usr/bin/env python3
"""
This module provides functions for serializing / deserializing
a custom object using pickle."""


class CustomObject:
    """
    A custom class that can be serialized and deserialized using pickle."""

    def __init__(self, name, age, is_student):
        """
        Initialize a CustomObject instance.
        Args:
            name (str): The name of the person.
            age (int): The age of the person.
            is_student (bool): Whether the person is a student.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Display the attributes of the object."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """Serialize the object to a file using pickle."""
        import pickle
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """Deserialize an object from a file using pickle."""
        import pickle
        try:
            with open(filename, 'rb') as f:
                return pickle.load(f)
        except Exception:
            return None
