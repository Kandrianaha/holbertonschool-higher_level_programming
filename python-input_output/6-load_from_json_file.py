#!/usr/bin/python3
"""This module write a function
that creates an Object from a "JSON file"""

import json


def load_from_json_file(filename):
    """This function creates an Object from a "JSON file"

    Args:
        filename (str): The name of the JSON file

    Returns:
        object: The object created from the JSON file
    """
    with open(filename, 'r') as f:
        return json.load(f)
