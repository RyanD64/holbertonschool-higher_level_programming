#!/usr/bin/python3
"""inherit from"""


def inherits_from(obj, a_class):
    """Return True if the object is an instance that inherited from 
    the specified class, otherwise false
    """
    if type(obj) is a_class or not isinstance(obj, a_class):
        return True
    else:
        return False
