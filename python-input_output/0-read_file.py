#!/usr/bin/python3
"""
This module reads a text file (UTF8) and prints it to stdout.
"""


def read_file(filename="my_file_0.txt"):
    """Read a text file (UTF8) and print it to stdout."""
    with open(filename, 'r', encoding='utf-8') as file:
        print(file.read(), end="")
