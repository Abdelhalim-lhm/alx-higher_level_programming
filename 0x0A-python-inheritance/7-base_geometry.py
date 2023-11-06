#!/usr/bin/python3
''' BaseGeometry module '''


class BaseGeometry:
    ''' BaseGeometry class definition '''
    def area(self):
        ''' Method area defintion '''
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        ''' integer_validator definition '''
        self.name = name
        self.value = value
        if not type(self.value) == int:
            raise TypeError(f"{self.name} must be an integer")
        if self.value <= 0:
            raise ValueError(f"{self.name} must be greater than 0")
