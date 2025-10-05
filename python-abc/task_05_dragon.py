#!/usr/bin/python3
"""
This module designs two mixin classes SwimMixin and FlyMixin
each equipped with methods swim and fly respectively.
"""


class SwimMixin:
    """Mixin class to provide swimming capability."""

    def swim(self):
        """Simulate swimming action."""
        print("The creature swims!")

class FlyMixin:
    """Mixin class to provide flying capability."""

    def fly(self):
        """Simulate flying action."""
        print("The creature flies!")

class Dragon(SwimMixin, FlyMixin):
    """A class representing a mythical creature that can both swim and fly."""

    def roar(self):
        """Simulate roaring"""
        print("The dragon roars!")
