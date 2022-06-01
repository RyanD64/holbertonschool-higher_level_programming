#!/usr/bin/python3
"""load from json file"""
import json


def load_from_json_file(filename):
    """create an object from a json file"""
    with open(filename, 'r', encoding="UTF-8") as read:
        return json.load(read)
