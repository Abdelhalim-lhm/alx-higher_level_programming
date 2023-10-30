#!/usr/bin/python3
''' Real definition of a rectangle '''


class Rectangle:
    ''' class that defines a rectangle '''
    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    @property
    def width(self):
        ''' getter definition '''
        return self.__width

    @width.setter
    def width(self, value):
        ''' setter definition '''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        ''' getter definition '''
        return self.__height

    @height.setter
    def height(self, value):
        ''' setter definition '''
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        str1 = ""
        if self.__width == 0 or self.__height == 0:
            return str1
        for i in range(self.__height):
            for j in range(self.__width):
                str1 += "#"
            if i < self.__height - 1:
                str1 += "\n"
        return str1

    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"
