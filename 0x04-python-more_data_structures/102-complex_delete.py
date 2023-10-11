#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if value in a_dictionary.values():
        return {key: v for key, v in a_dictionary.items() if v != value}
    else:
        return a_dictionary
