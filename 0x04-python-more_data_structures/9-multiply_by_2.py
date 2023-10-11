#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    dict_copy = a_dictionary.copy()
    for key, value in dict_copy.items():
        dict_copy[key] = value * 2
    return dict_copy
