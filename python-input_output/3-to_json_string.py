#!/usr/bin/python3
"""Write a function that returns the JSON representation of an object."""


import json


def to_json_string(my_obj):
    """return json"""
    json_string = json.dumps(my_obj)
    return json_string
