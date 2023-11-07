#!/usr/bin/python3
''' module definition '''
import json


def from_json_string(my_str):
    ''' json deseralisation function '''
    return json.loads(my_str)
