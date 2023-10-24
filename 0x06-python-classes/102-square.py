#!/usr/bin/python3
'''Area of a Square'''


class Square:
    '''Square Area class def'''
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        '''getter definition'''
        return self.__size

    @size.setter
    def size(self, value):
        '''setter definition'''
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size * self.__size

    def __eq__(self, square2):
        return self.area() == square2.area()

    def __ne__(self, square2):
        return self.area() != square2.area()

    def __gt__(self, square2):
        return self.area() > square2.area()

    def __ge__(self, square2):
        return self.area() >= square2.area()

    def __lt__(self, square2):
        return self.area() < square2.area()

    def __le__(self, square2):
        return self.area() <= square2.area()
