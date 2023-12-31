#!/usr/bin/python3
''' Low memory cost code '''


class LockedClass:
    '''
    prevents the user from dynamically
    creating new instance attributes
    '''

    __slots__ = ["first_name"]
