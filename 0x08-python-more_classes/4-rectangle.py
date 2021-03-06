#!/usr/bin/python3
"""class rectangle"""


class Rectangle:
    """define class rectangle"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """define area of the rectangle"""
        return (self.height * self.width)

    def perimeter(self):
        """define the perimeter of the rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return (self.height + self.width) * 2

    def __str__(self):
        """print the rectangle"""
        str = ""
        if self.__width == 0 or self.__height == 0:
            return str

        for a in range(self.__height):
            if a == self.__height - 1:
                str += (self.__width * '#')
            else:
                str += ((self.__width * '#') + '\n')
        return str

    def __repr__(self):
        """recreate an instance of rectangle with eval()"""
        la = str(self.__width)
        h = str(self.__height)

        res = "Rectangle(" + la + ", " + h + ")"
        return res
