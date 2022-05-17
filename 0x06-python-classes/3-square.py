#!/usr/bin/python3
"""defining square"""


class Square:
    """class that define a square"""
    def __init__(self, size=0):
        if type(size) != int:
            raise (TypeError('size must be an integer'))
        elif size < 0:
            raise (ValueError('size must be >= 0'))
        else:
            self.__size = size

    def area(self):
        size = self.__size
        return (size ** 2)