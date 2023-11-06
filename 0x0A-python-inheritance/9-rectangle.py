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
    
    def area(self):
        ''' area definition '''
        return self.__width * self.__height

    def __str__(self):
        ''' str representation '''
        return f"[Rectangle] {self.__width}/{self.__height}"
