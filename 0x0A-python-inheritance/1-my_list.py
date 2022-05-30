#!/usr/bin/python3
"""class that inherits form my_list"""


class MyList(list):
    """contains the list"""
    def print_sorted(self):
        print(sorted(self))
