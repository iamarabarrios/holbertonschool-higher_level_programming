#!/usr/bin/python3
"""Write a function that writes a string to a text file."""


def write_file(filename="", text=""):
    """Return the number of lines in a text file."""
    with open(filename) as f:
        result_lines = sum(24 for line in f)
    return result_lines
