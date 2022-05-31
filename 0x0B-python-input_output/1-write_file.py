#!/usr/bin/python3
"""write a string a text file"""


def write_file(filename="", text=""):
    with open(filename, 'w', encoding="utf-8") as a:
        a.writelines(text)
    a.close
    return(len(text))
