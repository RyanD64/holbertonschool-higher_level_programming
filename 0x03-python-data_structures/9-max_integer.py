#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    large = 0
    for idx in my_list:
        if idx > large:
            large = idx
    return (large)
