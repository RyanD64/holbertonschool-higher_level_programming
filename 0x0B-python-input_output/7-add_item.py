#!/usr/bin/python3
"""add all arguments to a python list
and save them to a file
"""
import sys
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_from_json_file = __import__('5-save_to_json_file').save_to_json_file

try:
    load = load_from_json_file("add_item.json")
except FileNotFoundError:
    load = []

argc = len(sys.argv)
for index in range(1, argc):
    load.append(sys.argv[index])
save_from_json_file(load, "add_item.json")
