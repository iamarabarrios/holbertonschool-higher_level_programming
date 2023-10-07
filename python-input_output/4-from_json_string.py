#!/usr/bin/python3
"""Write a function that returns an object"""


import json


def from_json_string(my_str):
    """Appends a string to the end of a UTF8 text file."""
    objec = json.loads(my_str)
    return objec
