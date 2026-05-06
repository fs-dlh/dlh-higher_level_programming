#!/usr/bin/python3
"""
Script that adds all arguments to a Python list and saves them to a JSON file.
"""

import sys
import os

# Import the required functions from previous tasks
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"
my_list = []

# Load existing list if the file exists
if os.path.exists(filename):
    try:
        my_list = load_from_json_file(filename)
    except Exception:
        # If loading fails for any reason, start with an empty list
        my_list = []

# Add all command-line arguments (skip the script name)
my_list.extend(sys.argv[1:])

# Save the updated list back to the file
save_to_json_file(my_list, filename)
