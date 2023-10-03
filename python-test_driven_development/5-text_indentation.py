#!/usr/bin/python3
"""prints a text with 2 new lines after each of these characters: ., ? and :"""


def text_indentation(text):
    """Print text with two new line after . ? :"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    output = ""
    characters_special = ".?:"

    for char in text:
        output += char
        if char in characters_special:
            output += "\n\n"
        elif char == "\n":
            output = output.rstrip()
            output += "\n"
    print(output, end="")
