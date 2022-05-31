#!/usr/bin/python3
"""return an object represented by
a json string
"""
import json


def from_json_string(my_str):
    return json.loads(my_str)
