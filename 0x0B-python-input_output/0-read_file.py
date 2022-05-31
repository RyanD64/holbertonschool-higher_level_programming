#!/usr/bin/python3
"""read a text file"""


def read_file(filename=""):
    with open(filename, 'r', encoding="utf-8") as a:
        for line in a:
            print(line, end='')
        print()
