#!/usr/bin/python3
"""A script that adds all arguments to Python list, and save them to a file"""


import json


def save_to_json_file(my_obj, filename):
    """Return the JSON representation of string object."""
    with open(filename, mode="w") as file:
        json.dump(my_obj, file)
