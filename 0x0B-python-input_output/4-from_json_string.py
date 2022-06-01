#!/usr/bin/python3
"""from json string"""
import json


def from_json_string(my_str):
    """return an object represented by
    a json string
    """
    return json.loads(my_str)
