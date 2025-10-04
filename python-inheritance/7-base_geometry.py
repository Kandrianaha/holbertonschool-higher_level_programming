#!/usr/bin/python3
"""
This module writes a class BaseGeometry that raises an Exception
and validates value name as always a string
"""


class BaseGeometry:
    """
    Writes a class BaseGeometry that raises an Exception
    """
    def area(self):
        """
        Raises an Exception with the message area() is not implemented
        """
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        """
        Validates value as always a string
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
