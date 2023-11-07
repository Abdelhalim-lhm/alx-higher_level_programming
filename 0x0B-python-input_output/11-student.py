#!/usr/bin/python3
''' module definition '''


class Student:
    ''' class student definition '''
    def __init__(self, first_name, last_name, age):
        ''' instance attribute definition '''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        ''' json dict definition '''
        try:
            for att in attrs:
                if type(att) is not str:
                    return self.__dict__
        except Exception:
            return self.__dict__
        new_dict = dict()
        for key, value in self.__dict__.items():
            if key in attrs:
                new_dict[key] = value
        return new_dict

    def reload_from_json(self, json):
        ''' reload json function '''
        for key,value in json.items():
            if key in self.__dict__:
                self.__dict__[key] = value
