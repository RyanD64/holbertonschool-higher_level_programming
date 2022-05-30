#!/usr/bin/python3
"""Myint inhetiting from int"""


class MyInt(int):
    """a class that inherit from int"""
    def __eq__(self, value):
        return super().__ne__(value)

    def __ne__(self, value):
        return super().__eq__(value)
