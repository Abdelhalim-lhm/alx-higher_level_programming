#!/usr/bin/python3
def multiple_returns(sentence):
    lenght = len(sentence)
    if sentence is None:
        F_letter = None
    else:
        F_letter = sentence[0]
    return (lenght, F_letter)
