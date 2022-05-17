#!/usr/bin/python3
class Square:
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        return self.__position
    
    @position.setter
    def position(self, value):
        message = "position must be a tuple of 2 positive integers"
        if type(value) != tuple or len(value) != 2:
            raise (TypeError(message))

        for item in value:
            if type(item) != int or item < 0:
                raise (TypeError(message))
        
        self.position = value

    def area(self):
        size = self.__size
        return (size ** 2)

    def my_print(self):
        size = self.__size
        if size == 0:
            print()

        for row in range(size):
            print('#' * size)
