#!/usr/bin/python3
"""This module appends a string to a text file (UTF8)"""


def append_write(filename="", text=""):
    """Append a string at the end of a text file (UTF8)"""

    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
