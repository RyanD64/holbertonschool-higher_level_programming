#!/usr/bin/python3
"""class rectangle"""

from models.base import Base


class Rectangle(Base):
    """class that inherits from base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """initialize all values from class rectangle"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """getter of width"""
        return(self.__width)

    @width.setter
    def width(self, value):
        """setter of width"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """getter of height"""
        return(self.__height)

    @height.setter
    def height(self, value):
        """setter of height"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """getter of x"""
        return(self.__x)

    @x.setter
    def x(self, value):
        """setter of x"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """getter of y"""
        return(self.__y)

    @y.setter
    def y(self, value):
        """setter of y"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """define the area of rectangle"""
        return self.__width * self.__height

    def display(self):
        """displat a rectangle with given parameters"""
        for c in range(self.__y):
            print()
        for a in range(self.__height):
            for d in range(self.__x):
                print(f" ", end="")
            for b in range(self.__width):
                print(f"#", end='')
            print()

    def __str__(self):
        """define a string to return the values of the degined rectangle"""
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - \
{self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        """public method that assign the attributes of the rectangle"""
        if len(kwargs) != 0:
            for e, f in kwargs.items():
                setattr(self, e, f)
        elif len(args) != 0:
            try:
                self.id = args[0]
                self.__width = args[1]
                self.__height = args[2]
                self.__x = args[3]
                self.__y = args[4]
            except IndexError:
                pass
        else:
            print()

    def to_dictionary(self):
        """return a dictionnary representation of the string of values"""
        return {'x': self.x, 'y': self.y, 'id': self.id,
                'height': self.height, 'width': self.width}
