#!/usr/bin/python3
"""Defines a JSON file-reading function."""


import json


def class_to_json(obj):

    if hasattr(obj, "__dict__"):
        obj_dict = obj.__dict__
        serializable_dict = {}

        for key, value in obj_dict.items():
            if isinstance(value, (list, dict, str, int, bool)):
                serializable_dict[key] = value
        return serializable_dict
    else:
        raise ValueError("Object is not serializable")
