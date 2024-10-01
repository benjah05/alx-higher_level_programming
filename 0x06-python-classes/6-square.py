#!/usr/bin/python3
class Square:
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position
    @property
    def size(self):
        return (self.__size)
    @size.setter
    def size(self, value):
        if (isinstance(value, int) == False):
            raise TypeError("size must be an integer")
        if (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value
    @property
    def position(self):
        return (self.__position)
    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) and len(value) == 2 and all(isinstance(i, int) and i > 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
    def area(self):
        return (self.__size ** 2)
    def my_print(self):
        if (self.__size == 0):
            print("\n")
        for i in self.__position:
            for j in self.__position:
                print("#", end="")
                if (j == self.__size - 1):
                    print()
