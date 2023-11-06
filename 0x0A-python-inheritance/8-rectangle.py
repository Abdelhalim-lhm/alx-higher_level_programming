#!/usr/bin/python3
''' BaseGeometry importation module '''
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    ''' Class Rectangle definition '''
    def __init__(self, width, height):
        ''' Regtangle definition '''
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
