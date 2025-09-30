#!/usr/bin/python3
"""
This module defined a class MyList that inherits from the built-in list class.
It adds a method to print list in sorted order without modifying the original list.
"""


class MyList(list)
"""
MyList class that extends the built-in list.
"""
    def print_sorted(self):
    """
    Prints the list in ascending sorted order
    without changing the original list.
    Assumes all elemnts are integers.
    """
    print(sorted(self))
