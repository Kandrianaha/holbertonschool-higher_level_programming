#!/usr/bin/python3
"""
This module Write a function that returns the list
of available attributes and methods of an object
"""


def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.

    Args:
        obj: The object to inspect.

    Returns:
        A list of strings representing the names of attributes and methods.
    """
    return dir(obj)

