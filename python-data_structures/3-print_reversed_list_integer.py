#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):

    if my_list:
        other_list = my_list.copy()
        other_list.reverse()

        for i in other_list:
            print("{:d}".format(i))
