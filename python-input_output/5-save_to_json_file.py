#!/usr/bin/python3
"""Function that writes an Object to a text file, using a JSON."""


import json


def save_to_json_file(my_obj, filename):
    """Return the JSON representation of string object."""
    with open(filename, mode="w") as file_json:
        json.dump(my_obj, file_json)
