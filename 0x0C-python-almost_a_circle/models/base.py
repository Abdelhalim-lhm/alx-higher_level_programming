#!/usr/bin/python3
''' base module definition '''
import json


class Base:
    ''' Class Base definition '''
    __nb_objects = 0

    def __init__(self, id=None):
        ''' Class Base constructor '''
        self.id = id
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        ''' Dictionnary to Json string '''
        if not list_dictionaries:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        ''' save to file definition '''
        filename = "{}.json".format(cls.__name__)
        if list_objs:
            list_dicts = [obj.to_dictionary() for obj in list_objs]
            with open(filename, 'w', encoding='utf-8') as my_file:
                return my_file.write(cls.to_json_string(list_dicts))
        else:
            with open(filename, 'w', encoding='utf-8') as my_file:
                return my_file.write(cls.to_json_string(list_objs))

    @staticmethod
    def from_json_string(json_string):
        '''JSON string to dictionary'''
        if not json_string:
            return []
        else:
            return json.loads(json_string)
