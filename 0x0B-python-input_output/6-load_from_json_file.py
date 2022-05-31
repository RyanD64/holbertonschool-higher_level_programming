#!/usr/bin/python3
"""create an object from a json file"""
import json


def load_from_json_file(filename):
    with open(filename, 'r', encoding="UTF-8") as read:
        return json.load(read)
