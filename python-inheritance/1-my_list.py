#!/usr/bin/python3
"""Write a class MyList that inherits from list."""


class MyList(list):
    """Implements printing."""

    def print_sorted(self):
        """Print a list in ascending order."""
        sort_list = self.copy()
        sr_list = sorted(sort_list)
        print(sort_list)
