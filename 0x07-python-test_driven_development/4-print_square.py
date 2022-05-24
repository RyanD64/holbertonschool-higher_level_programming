#!/usr/bin/python3
"""print_square"""


def print_square(size):
    """print a square of a given size with the # character"""
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size == 0:
        return None

    for rox in range(size):
        print('#' * size)
