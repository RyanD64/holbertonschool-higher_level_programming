#!/usr/bin/python3
"""class Base"""
import json
import csv


class Base:
    """creating the base of all others classes
    in the project
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """initializing class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """return json strings"""
        if type(list_dictionaries) != str or len(list_dictionaries) == 0:
            return []
        return json.loads(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """"""
        if cls.__name__ == "Rectangle":
            tmp = cls(1, 1)
        if cls.__name__ == "Square":
            tmp = cls(1)
        tmp.update(list_objs)
        return tmp
