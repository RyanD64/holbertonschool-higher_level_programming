#!/usr/bin/python3
"""inherit from
"""


def inherits_from(obj, a_class):
    """Function that Return True if the object is an instance that inherited from
    the specified class(directly or indirectly),
    otherwise false
    """
    if type(obj) is a_class or not isinstance(obj, a_class):
        return True
    else:
        return False
