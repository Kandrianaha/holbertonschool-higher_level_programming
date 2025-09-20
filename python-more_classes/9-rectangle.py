#!/usr/bin/python3
"""
This module defines a Rectangle class with width and height
It can compare rectangles by area and create a square.
"""


class Rectangle:
    """A class that defines a rectangle by width and height."""
    number_of_instances = 0  # Class variable to track number of instances
    print_symbol = '#'       # Symbol used for string representation

    def __init__(self, width=0, height=0):
        """Initializes the rectangle with width and height."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Getter for the width attribute."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for the width attribute with validation."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter for the height attribute."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for the height attribute with validation."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates and returns the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Calculates and returns the perimeter of the rectangle."""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """Returns a string representation of the rectangle
        using '#' characters."""
        if self.width == 0 or self.height == 0:
            return ""
        symbol = str(self.print_symbol)
        return '\n'.join([symbol * self.width for _ in range(self.height)])

    def __repr__(self):
        """Returns a string that can recreate the rectangle using eval()."""
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """Prints a message when the rectangle is deleted."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the rectangle with the greater area or rect_1 if equal."""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """Creates a square rectangle (width == height == size)."""
        return cls(size, size)
