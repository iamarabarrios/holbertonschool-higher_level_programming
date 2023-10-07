#!/usr/bin/python3
"""Write a function that appends a string at the end of a text file."""


def append_write(filename="", text=""):
    """Append a string to the end of a text file."""
    with open(filename, mode="a", encoding="utf-8") as file:
        characters_add = file.write(text)
    return characters_add
