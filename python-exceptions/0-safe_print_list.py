#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):

    elements_printed_count = 0
    try:
        for i in range(x):
            print(my_list[i], end="")
            elements_printed_count += 1
    except IndexError:
        pass
    print()
    return elements_printed_count
