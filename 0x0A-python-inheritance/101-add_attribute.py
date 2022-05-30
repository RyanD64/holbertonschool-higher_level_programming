#!/usr/bin/python3
"""add new attribute to an object"""


def add_attribute(a_class, name, value):
    cant_add = {int, str, float, list, dict, tuple, frozenset, type, object}
    if type(a_class) in cant_add:
        raise TypeError("can't add new attribute")

    a_class.__setattr__(name, value)
