#!/usr/bin/python3
''' module Myint definition '''


class MyInt(int):
    ''' Myint rebel definition '''
    def __eq__(self, value):
        ''' eq became no eq definition '''
        return not super().__eq__(value)

    def __ne__(self, value):
        ''' ne become eq definition '''
        return not super().__ne__(value)
