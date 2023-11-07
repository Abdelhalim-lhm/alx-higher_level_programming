#!/usr/bin/python3
''' module definition '''
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


my_list = list(sys.argv[1:])
try:
    my_data = load_from_json_file('add_item.json')
except Exception:
    my_data = []
my_data.extend(my_list)
save_to_json_file(my_data, 'add_item.json')
