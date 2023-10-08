#!/usr/bin/python3
"""Defines a JSON file-reading function."""


def class_to_json(obj):
    """
    Returns the dictionary description."""
    return {key: value for key, value in obj.__dict__.items() if
            isinstance(value, (list, dict, str, int, bool))}
