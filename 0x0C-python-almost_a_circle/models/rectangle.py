#!/usr/bin/python3
''' Module definition '''
from models.base import Base


class Rectangle(Base):
    ''' class rectangle definition '''
    def __init__(self, width, height, x=0, y=0, id=None):
        ''' Rectangle constructor '''
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")

    def area(self):
        ''' Area of the rectangle '''
        return self.__width * self.__height

    def display(self):
        ''' print rectangle '''
        for i in range(self.__height):
            for j in range(self.__width):
                print("#", end="")
            print()
