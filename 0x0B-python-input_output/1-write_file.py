#!/usr/bin/python3
"""write file"""


def write_file(filename="", text=""):
    """write a strig to a text file"""
    with open(filename, 'w', encoding="utf-8") as a:
        a.writelines(text)
    a.close
    return(len(text))
