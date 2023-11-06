#!/usr/bin/python3
''' BaseGeometry importation module '''
Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    ''' Sqaure class definition '''
    def __init__(self, size):
        ''' square definition '''
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        ''' method aream definition '''
        return self.__size * self.__size
