#!/usr/bin/python3
''' module definition '''


def append_write(filename="", text=""):
    ''' append funtion definition '''
    with open(filename, 'a', encoding='utf-8') as my_file:
        return my_file.write(text)
