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
        '''position setter'''
        if (not isinstance(value, tuple) or len(value) != 2
                or not all(isinstance(val, int) for val in value)
                or not all(val >= 0 for val in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(self.position[1]):
                print()
            for i in range(self.__size):
                for j in range(self.__position[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print()
