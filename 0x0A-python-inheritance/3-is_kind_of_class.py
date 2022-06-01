#!/usr/bin/python3
"""is kind of class"""


def is_kind_of_class(obj, a_class):
    """Return True if the object is an instance of the
    specified class or an inheritnce of the class"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
