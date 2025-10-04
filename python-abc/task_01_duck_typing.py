#!/usr/bin/python3
"""
This module creates an abstract class named Shape
with two abstract methods: area and perimeter.
"""

from abc import ABC, abstractmethod
import math

class Shape(ABC):
    """
    An abstract base class representing a geometric shape.
    """

    @abstractmethod
    def area(self):
        """
        Calculate the area of the shape.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Calculate the perimeter of the shape.
        """
        pass

class Circle(Shape):
    """
    A class representing a circle, inheriting from Shape.
    """

    def __init__(self, radius):
        """
        Initialize the Circle with a given radius.

        Args:
            radius (float): The radius of the circle.
        """
        self.radius = radius

    def area(self):
        """
        Calculate the area of the circle.

        Returns:
            float: The area of the circle.
        """
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """
        Calculate the perimeter (circumference) of the circle.

        Returns:
            float: The perimeter of the circle.
        """
        return 2 * math.pi * self.radius

class Rectangle(Shape):
    """
    A class representing a rectangle, inheriting from Shape.
    """
    def __init__(self, width, height):
        """
        Initialize the Rectangle with a given width and height.

        Args:
            width (float): The width of the rectangle.
            height (float): The height of the rectangle.
        """
        self.width = width
        self.height = height

    def area(self):
        """
        Calculate the area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calculate the perimeter of the rectangle.
        """
        return 2 * (self.width + self.height)

def shape_info(shape):
    """
    Print the area and perimeter of a given shape.

    Args:
        shape (Shape): An instance of a class that inherits from Shape.
    """
    if not isinstance(shape, Shape):
        raise TypeError("The object must be an instance of a subclass of Shape.")
    
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())

if __name__ == "__main__":
    circle = Circle(radius=5)
    rectangle = Rectangle(width=4, height=7)

    shape_info(circle)
    shape_info(rectangle)
