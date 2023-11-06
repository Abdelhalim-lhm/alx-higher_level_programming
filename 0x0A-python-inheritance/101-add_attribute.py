#!/usr/bin/python3
''' module definition '''


def add_attribute(obj, attr, value):
    ''' add_attribute definition '''
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, attr, value);
