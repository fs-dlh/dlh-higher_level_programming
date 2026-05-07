#!/usr/bin/env python3
"""
This module provides functions for serializing data to XML file.
"""

import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
    """
    Serialize the given data to XML and save it to the specified file.

    Args:
        dictionary (dict): The dictionary to be serialized.
        filename (str): The name of the XML file to save the serialized data.
    """
    root = ET.Element("root")
    
    for key, value in dictionary.items():
        item = ET.SubElement(root, "item", key=key)
        item.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename, encoding='utf-8', xml_declaration=True)

def deserialize_from_xml(filename):
    """
    Load and deserialize data from the specified XML file.

    Args:
        filename (str): The name of the XML file to load the data from.

    Returns:
        dict: The deserialized data as a dictionary.
    """
    tree = ET.parse(filename)
    root = tree.getroot()

    data = {}
    for item in root.findall("item"):
        key = item.get("key")
        value = item.text
        data[key] = value

    return data
