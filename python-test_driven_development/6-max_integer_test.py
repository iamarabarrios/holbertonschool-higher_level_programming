#!/usr/bin/python3
"""add Unittests"""


def max_integer(list=[]):
    """Function for find and return the max integer in the list of integer"""
    if len(list) == 0:
        return None

    result = list[0]
    i = 1

    while i < len(list):
        if list[i] > result:
            result = list[i]
        i += 1
    return result
