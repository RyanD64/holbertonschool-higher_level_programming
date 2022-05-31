#!/usr/bin/python3
"""append a string at the end of a text file"""


def append_write(filename="", text=""):
    with open(filename, 'a', encoding="utf-8") as a:
        a.write(text)
        return len(text)
