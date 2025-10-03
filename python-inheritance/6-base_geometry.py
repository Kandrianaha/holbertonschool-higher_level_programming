#!/usr/bin/python3
"""
This module writes a class BaseGeometry that raises an exception.
"""


class BaseGeometry:
    """
    A class representing basic geometric shapes.
    Raises: Exception with message.
    """
    def area(self):
        """
        Calculates the area of the geometric shape.
        """
        raise Exception("area() is not implemented")
