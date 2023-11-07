#!/usr/bin/python3
''' module definition '''


class Student:
    ''' class student definition '''
    def __init__(self, first_name, last_name, age):
        ''' instance definition '''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    def to_json(self):
        ''' json dict definition '''
        return self.__dict__
