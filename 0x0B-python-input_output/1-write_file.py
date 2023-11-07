#!/usr/bin/python3
''' module definition '''


def write_file(filename="", text=""):
    ''' write_file definition '''
    with open(filename, 'w', encoding='utf-8') as my_file:
        return my_file.write(text)
