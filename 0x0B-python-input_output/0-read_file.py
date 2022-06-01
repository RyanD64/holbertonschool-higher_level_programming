#!/usr/bin/python3
"""read file"""


def read_file(filename=""):
    """read a text file"""
    with open(filename, 'r', encoding="utf-8") as a:
        for line in a:
            print(line, end='')
        print()
