#!/usr/bin/python3
"""function that adds two integers"""


def add_integer(a, b=98):
    """add two integers
    convert to int if float
    if a or b are not an int, raise a type error
    """
    if type(a) == float or type(b) == float:
        a = int(a)
        b = int(b)

    if type(a) != int:
        raise TypeError("a must be an integer")
    elif type(b) != int:
        raise TypeError("b must be an integer")
    else:
        return(a + b)
