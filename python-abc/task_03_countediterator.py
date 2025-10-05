#!/usr/bin/python3
"""
This module creates a class names CountedIterator
that extends the built-in iterator obtaines from the iter function.
"""


class CountedIterator:
    """
    A class that extends the built-in iterator obtained from the iter function.
    It keeps track of the number of items that have been iterated over.
    """

    def __init__(self, iterable):
        """
        Initializes the CountedIterator with an iterable.

        Args:
            iterable: An iterable object (e.g., list, tuple, string).
        """
        self._iterator = iter(iterable)
        self._count = 0

    def __iter__(self):
        """
        Returns the iterator object itself.

        Returns:
            The iterator object.
        """
        return self

    def __next__(self):
        """
        Returns the next item from the iterator and increments the count.

        Returns:
            The next item from the iterator.

        Raises:
            StopIteration: If there are no more items to iterate over.
        """
        item = next(self._iterator)  # May raise StopIteration
        self._count += 1
        return item

    def get_count(self):
        """
        Returns the number of items that have been iterated over so far.

        Returns:
            The count of iterated items.
        """
        return self._count
