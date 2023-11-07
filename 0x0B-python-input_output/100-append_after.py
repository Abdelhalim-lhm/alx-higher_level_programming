#!/usr/bin/python3
''' module definiton '''


def append_after(filename="", search_string="", new_string=""):
    ''' append_after definition '''
    new_file = []
    with open(filename, 'a', encoding='utf-8') as my_file:
        pass
    with open(filename, 'r', encoding='utf-8') as my_file:
        for line in my_file:
            new_file.append(line)
            if search_string in line:
                new_file.append(new_string)
    with open(filename, 'w', encoding='utf-8') as my_file:
        my_file.writelines(new_file)
