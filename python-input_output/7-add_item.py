#!/usr/bin/python3
"""A script that adds all arguments to Python list, and save them to a file"""


import json
import sys


def save_to_json_file(my_obj, filename):
    """Return the JSON representation of string object."""
    with open(filename, mode="w") as file:
        json.dump(my_obj, file)

if __name__ == "__main__":
    my_list = []

    for arg in sys.argv[1:]:
        my_list.append(arg)

    save_to_json_file(my_list, "add_item.json")
