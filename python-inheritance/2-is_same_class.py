#!/usr/bin/python3
"""
This module defines a function to check if an object is exactly an instance of a specified class.
"""


def is_same_class(obj, a_class):
    """Function that returns True if the object is exactly an instance of the
    specified class ; otherwise False.
    Args:
        obj: The object to check.
        a_class: The class to match the type of obj to.
    Returns:
        True if obj is exactly an instance of a_class, otherwise False.
    """
    return type(obj) is a_class
