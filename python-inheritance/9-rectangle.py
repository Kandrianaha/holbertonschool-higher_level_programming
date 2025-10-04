#!/usr/bin/python3
"""
This module writes a class Rectangle that ingherits from BaseGeometry
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    A class representing a rectangle, inheriting from BaseGeometry.
    """
    def __init__(self, width, height):
        """
        Instantiation with width and height of Rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Returns the area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns string representation of the rectangle
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
