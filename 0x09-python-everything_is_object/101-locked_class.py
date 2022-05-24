#!/usr/bin/python3
"""Locked class"""


class LockedClass:
    """cannot create dynamicly new instance arributes
        except first name
    """
    def __setattr__(self, attribute, value):
        if attribute == "first_name":
            self.__dict__[attribute] = value
        else:
            raise AttributeError("'LockedClass' object has no attribute '"
                                 + attribute + "'")
