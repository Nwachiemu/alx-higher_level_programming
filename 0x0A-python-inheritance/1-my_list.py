#!/usr/bin/python3
"""Defines an inherited list class MyList."""


class MyList(list):
    """Implementation of sorted list"""

    def print_sorted(self):
        """Print a list"""
        print(sorted(self))
