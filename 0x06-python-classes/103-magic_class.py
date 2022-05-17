#!/usr/bin/python3
"""magic class"""
import math



class MagicClass:
    """define area and circumference of a circle"""
    def __init__(self, radius):
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be an number')
        self.__radius = radius

    
    def area(self, radius):
        return self.radius ** 2 * math.pi

    
    def circumference(self, radius):
        return 2 * math.pi *self.__radius