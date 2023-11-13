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
