#!/usr/bin/python
''' module is_the_same '''


def is_same_class(obj, a_class):
    ''' method definition '''
    if type(obj) == a_class:
        return True
    else:
        return False
