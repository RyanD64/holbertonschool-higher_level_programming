#!/usr/bin/python3
"""append_after"""


def append_after(filename="", search_string="", new_string=""):
    with open(filename, mode="r+", encoding="utf-8") as read:
        tmp = read.readlines()

    count = 0
    with open(filename, mode="w", encoding="utf-8") as write:
        for lines in tmp:
            count += 1
            if search_string in lines:
                tmp.insert(count, new_string)
        for lines in tmp:
            write.write(lines)
