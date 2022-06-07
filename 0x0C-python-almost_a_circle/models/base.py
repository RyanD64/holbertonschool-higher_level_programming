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
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """return the list of the json string representation"""
        if type(json_string) != str or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """write the json representation of list_objs to a file"""
        with open(cls.__name__ + ".json", mode="w") as write_file:
            if list_objs is None:
                write_file.write("[]")
            else:
                write_file.write(cls.to_json_string(
                                 [item.to_dictionary() for item in list_objs]))

    @classmethod
    def create(cls, **dictionary):
        """return an instance with all atributes already set"""
        if cls.__name__ == "Rectangle":
            tmp = cls(1, 1)
        if cls.__name__ == "Square":
            tmp = cls(1)
        tmp.update(**dictionary)
        return tmp

    @classmethod
    def load_from_file(cls):
        """return a list of instances"""
        res = []
        with open(cls.__name__ + ".json", mode="r") as read_file:
            text = read_file.read()
        text = cls.from_json_string(text)
        for item in text:
            if type(item) == dict:
                res.append(cls.create(**item))
            else:
                res.append(item)
        return
