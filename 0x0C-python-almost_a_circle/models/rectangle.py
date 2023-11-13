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
        for i in range(self.__height + self.__y):
            if i < self.__y:
                print()
            else:
                for j in range(self.__width + self.__x):
                    if j < self.__x:
                        print(" ", end="")
                    else:
                        print("#", end="")
                print()

    def __str__(self):
        ''' str presentation '''
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - \
{self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        ''' update args and kwargs '''
        if args:
            if len(args) >= 1:
                self.id = args[0] if args[0] is not None else self.id
            if len(args) >= 2:
                self.width = args[1] if args[1] is not None else self.width
            if len(args) >= 3:
                self.height = args[2] if args[2] is not None else self.height
            if len(args) >= 4:
                self.x = args[3] if args[3] is not None else self.x
            if len(args) >= 5:
                self.y = args[4] if args[4] is not None else self.y

        for key, value in kwargs.items():
            if key == 'id' and value is not None:
                self.id = value
            if key == 'width' and value is not None:
                self.width = value
            if key == 'height' and value is not None:
                self.height = value
            if key == 'x' and value is not None:
                self.x = value
            if key == 'y' and value is not None:
                self.y = value
