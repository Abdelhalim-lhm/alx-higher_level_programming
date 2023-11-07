#!/usr/bin/python3
''' module definition '''
import json


def save_to_json_file(my_obj, filename):
    ''' writes an Object to a text file, using a JSON '''
    with open(filename, 'w', encoding='utf-8') as my_file:
        return my_file.write(json.dumps(my_obj))
