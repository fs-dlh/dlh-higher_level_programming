#!/usr/bin/env python3
"""
This module provides functions for serializing and converting data
from CSV to JSON format."""


import csv
import json


def convert_csv_to_json(csv_file):
    """
    Convert data from a CSV file to JSON format and save it to a file.

    Args:
        csv_file (str): Name of the CSV file to be converted.
    """
    try:
        with open(csv_file, 'r') as f:
            reader = csv.DictReader(f)
            data = list(reader)

        with open('data.json', 'w') as json_file:
            json.dump(data, json_file, indent=4)
    except Exception:
        return None
