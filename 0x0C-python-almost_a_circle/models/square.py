#!/usr/bin/python3
"""class Square"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """class that inherits from rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """initialize all values from class square"""
        super().__init__(width=size, height=size, x=x, y=y, id=id)

    @property
    def size(self):
        """getter of size"""
        return(self.width)

    @size.setter
    def size(self, value):
        """setter of size"""
        self.width = value
        self.height = value

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
        """define the area of a square"""
        return self.width * self.width

    def display(self):
        """display a square with given parameters"""
        for c in range(self.__y):
            print()
        for a in range(self.width):
            for d in range(self.__x):
                print(f" ", end="")
            for b in range(self.width):
                print(f"#", end='')
            print()

    def __str__(self):
        """define a string to print the values of the square"""
        return f"[Square] ({self.id}) {self.__x}/{self.__y} - \
{self.width}"

    def update(self, *args, **kwargs):
        """public method that assign the attributes of the square"""
        if len(kwargs) != 0:
            for g, h in kwargs.items():
                setattr(self, g, h)
        elif len(args) != 0:
            try:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
            except IndexError:
                pass
        else:
            print()

        def to_dictionary(self):
            """return a dictionnary representation"""
            return {'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y}
