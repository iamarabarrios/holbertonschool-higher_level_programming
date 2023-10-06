#!/usr/bin/python3
"""returns the list of available attributes and methods of an object"""


def lookup(obj):
    """Return list with objects available attributes"""
    return dir(obj)
