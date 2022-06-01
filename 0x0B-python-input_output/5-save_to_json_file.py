#!/usr/bin/python3
"""save to json file"""
import json


def save_to_json_file(my_obj, filename):
    """write an object to a text file
    in json representation
    """
    with open(filename, 'w', encoding="UTF-8") as save:
        json.dump(my_obj, save)
