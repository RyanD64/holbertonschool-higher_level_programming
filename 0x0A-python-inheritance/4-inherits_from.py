#!/usr/bin/python3
"""inherit from"""


def inherits_from(obj, a_class):
    if type(obj) is a_class or not isinstance(obj, a_class):
        return True
    else:
        return False
