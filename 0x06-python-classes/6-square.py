#!/usr/bin/python3
'''Area of a Square'''


class Square:
    '''Square Area class def'''
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        '''geting size'''
        return self.__size

    @size.setter
    def size(self, value):
        '''setter definition'''
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        '''geting position'''
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple):
            if not len(value) != 2:
                if not (isinstance(value[0], int) or
                        isinstance(value[0], int)):
                    if not (value[0] >= 0 or
                            value[1] >= 0):
                        raise TypeError
                    ("position mustbe a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__position[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print()
