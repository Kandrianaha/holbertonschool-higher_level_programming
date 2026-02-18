#!/usr/bin/python3
"""This module write a function that writes
an Object to a text file, using a JSON representation"""

import json


def save_to_json_file(my_obj, filename):
    """Writes an Object to a text file, using a JSON representation

    Args:
        my_obj: The object to write
        filename: The name of the file to write to
    """

    with open(filename, 'w') as f:
        json.dump(my_obj, f)
