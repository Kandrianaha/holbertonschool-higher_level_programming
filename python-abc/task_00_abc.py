#!/usr/bin/python3
"""
This module creates an abstract class names Animal
using the ABC package.
"""


from abc import ABC, abstractmethod


class Animal(ABC):
    """
    An abstract class representing an animal.
    """
    @abstractmethod
    def sound(self):
        """
        An abstract method that should be implemented by subclasses
        to return the sound made by the animal.
        """
        pass

class Dog(Animal):
    """
    A class representing a dog, inheriting from Animal.
    """
    def sound(self):
        """
        Returns the sound made by the dog.
        """
        return "Woof!"
    
class Cat(Animal):
    """
    A class representing a cat, inheriting from Animal.
    """
    def sound(self):
        """
        Returns the sound made by the cat.
        """
        return "Meow!"

bobby = Dog()
garfield = Cat()

print(bobby.sound())  # Output: Woof!
print(garfield.sound())  # Output: Meow!

print(isinstance(bobby, Animal))  # Output: True
print(isinstance(garfield, Animal)) #Output: True
