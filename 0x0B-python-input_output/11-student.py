#!/usr/bin/python3
"""class student"""


class Student:
    """contains student data"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None or type(attrs) != list:
            return self.__dict__
        else:
            tmp = {}
            for element in attrs:
                if type(element) != str:
                    return self.__dict__
                if element in self.__dict__.keys():
                    tmp[element] = self.__dict__[element]
            return tmp

    def reload_from_json(self, json):
        for items in json.keys():
            self.__dict__[items] = json[items]
