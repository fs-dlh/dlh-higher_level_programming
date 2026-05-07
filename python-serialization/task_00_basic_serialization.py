#!/usr/bin/env python3
"""
This module provides functions for serializing data to JSON,
as well as loading and deserializing data from a JSON file.
"""

import json


def serialize_and_save_to_file(data, filename):
    """
    Serialize the given data to JSON and save it to the specified file."""

    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """
    Load and deserialize data from the specified JSON file.
    """

    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
