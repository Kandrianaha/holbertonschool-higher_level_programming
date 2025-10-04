#!/usr/bin/python3
"""
This module writes a class square that inherits from Rectangle
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A class representing a square, inheriting from Rectangle.
    """
    def __init__(self, size):
        """
        Initializes a Square instance with size.

        Args:
            size (int): The size of the square's sides.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than or equal to 0.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        Returns the area of the square.
        """
        return self.__size ** 2
