#!/usr/bin/python3
"""append write"""


def append_write(filename="", text=""):
    """append a string at the end of a text file"""
    with open(filename, 'a', encoding="utf-8") as a:
        a.write(text)
        return len(text)
