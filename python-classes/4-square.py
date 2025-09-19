#!/usr/bin/python3
"""
This module defines a Square by its size.
"""

class Square:
    """
    Defining Square class with a private instance attribute size.
    """
    def __init__(self, size=0):
        """
        Initializes the square with a given size.

        Args:
            size (int): The size of the square's sides. Default is 0.

        """
        self.__size = size

    @property
    def size(self):
        """
        Getter for the size property.

        Returns:
            int: The size of the square.
        """
        return self.__size
    
    @size.setter
    def size(self, value):
        """
        Setter for the size property with validation.

        Args:
            value (int): The new size of the square's sides.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size
