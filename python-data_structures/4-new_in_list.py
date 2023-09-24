#!/usr/bin/python3


def new_in_list(my_list, idx, element):
    other_list = my_list.copy()

    if idx < 0 or idx >= len(my_list):
        return other_list
    other_list[idx] = element
    return other_list
