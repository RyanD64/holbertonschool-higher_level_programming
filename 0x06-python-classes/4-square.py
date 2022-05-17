#!/usr/bin/python3
"""define square"""


class Square:
    """class square"""
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise (TypeError('size must be an integer'))
        elif value < 0:
            raise (ValueError('size must be >= 0'))
        else:
            self.__size = value

    def area(self):
        size = self.__size
        return (size ** 2)
