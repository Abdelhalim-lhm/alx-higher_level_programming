#!/usr/bin/python3
def multiple_returns(sentence):
    lenght = len(sentence)
    if lenght == 0:
        F_letter = None
    F_letter = sentence[0]
    return (lenght, F_letter)
