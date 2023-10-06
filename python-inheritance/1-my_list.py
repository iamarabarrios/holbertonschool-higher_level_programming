#!/usr/bin/python3
"""Write a class MyList that inherits from list."""


class MyList(list):
    """Implements printing."""

    def print_sorted(self):
        """Print a list in ascending order."""
        sorted_list = sorted(self)
        print(sorted_list)
