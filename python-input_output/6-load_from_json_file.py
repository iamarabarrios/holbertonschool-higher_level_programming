#!/usr/bin/python3
"""Write a function that creates an Object from a “JSON file”:"""


import json


def load_from_json_file(filename):
    """Load an object from a JSON file."""
    with open(filename, mode="r") as file_json:
        load_obj = json.load(file_json)
    return load_obj
