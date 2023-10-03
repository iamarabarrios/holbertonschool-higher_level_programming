#!/usr/bin/python3
"""prints a text with 2 new lines after each of these characters: ., ? and :"""


def text_indentation(text):
    """Print text with two new line after . ? :"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    output = ""
    characters_special = ".?:"

    for char in text:
        if char in characters_special:
            if char in characters_special:
                output += char + "\n\n"
            else:
                if char != " ":
                    output += char
                    if char == "\n":
                    continue
                if char not in characters_special:
                    output += " "
    print(output, end="")
