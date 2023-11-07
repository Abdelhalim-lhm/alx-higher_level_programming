#!/usr/bin/python3
''' module definition '''


def read_file(filename=""):
    ''' read_file definition '''
    with open(filename, encoding='utf-8') as my_file:
        print(my_file.read(), end="")
