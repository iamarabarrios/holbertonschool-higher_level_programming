#!/usr/bin/python3
"""Defines a JSON file-reading function."""


import json


def class_to_json(obj):
    """Convert an instance of MyClass to a JSON serializable dictionary"""
    return obj.__dict__
