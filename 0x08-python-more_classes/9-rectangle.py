#!/usr/bin/python3
''' Real definition of a rectangle '''


class Rectangle:
    ''' class that defines a rectangle '''
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

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
        return self.width * self.height

    def perimeter(self):
        if not self.width or not self.height:
            return 0
        else:
            return 2 * (self.width + self.height)

    def __str__(self):
        str1 = ""
        if not self.width or not self.height:
            return str1
        for i in range(self.height):
            for j in range(self.width):
                str1 += str(self.print_symbol)
            if i < self.height - 1:
                str1 += "\n"
        return str1

    def __repr__(self):
        return f"Rectangle({str(self.width)}, {str(self.height)})"

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        return cls(size, size)