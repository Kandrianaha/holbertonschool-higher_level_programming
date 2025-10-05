#!/usr/bin/python3
"""
This module construct a FlyingFish class
that inherits from both Fish and Bird classes.
"""


class Fish:
    """Fish class with swim method."""

    def swim(self):
        """Simulate swimming action."""
        print("The fish is swimming.")

    def habitat(self):
        """Return the habitat of the fish."""
        print("The fish lives in water.")

class Bird:
    def fly(self):
        """Simulate flying action."""
        print("The bird is flying.")
    
    def habitat(self):
        """Return the habitat of the bird."""
        print("The bird lives in the sky.")

class FlyingFish(Fish, Bird):
    def fly(self):
        """Overrrides the fly method."""
        print("The flying fish is soaring!.")

    def swim(self):
        """Overrides the swim method."""
        print("The flying fish is swimming!.")

    def habitat(self):
        """Return the habitat of the flying fish."""
        print("The flying fish lives in both water and the sky.")

flying_fish = FlyingFish()
flying_fish.swim()  # Inherited from Fish
flying_fish.fly()   # Inherited from Bird
flying_fish.habitat()  # Overridden method

print(FlyingFish.mro())  # Display the method resolution order
