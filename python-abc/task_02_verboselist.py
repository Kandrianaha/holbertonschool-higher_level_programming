#!/usr/bin/python3
"""
This module creates a class VerboseList that extends the built-in list class.
The VerboseList class overrides the append method to print a message each time
an item is added to the list.
"""


class VerboseList(list):
    """
    A list subclass that prints a message when an item is appended.
    """

    def append(self, item):
        """
        Appends an item to the list and prints a message.

        Args:
            item: The item to be appended to the list.
        """
        super().append(item)
        print(f"Added {item} to {self[:]}")

    def extend(self, iterable):
        """
        Extends the list by appending elements from the iterable and prints a message.

        Args:
            iterable: An iterable whose elements are to be added to the list.
        """
        super().extend(iterable)
        print(f"Extended {self[:]} with {list(iterable)}")

    def remove(self, item):
        """
        Removes the first occurrence of a value from the list and prints a message.
        """
        if item in self:
            super().remove(item)
            print(f"Removed [{item}] from {self[:]}")
        else:
            print(f"Item {item} not found in {self[:]}")
    
    def pop(self, index=-1):
        """
        Removes and returns the item at the given index from the list and prints a message.
        """
        if len(self) == 0:
            print("Cannot pop from an empty list.")
            return None
        item = self[index]
        print(f"Popped {item} from {self[:]}")
        return super().pop(index)
