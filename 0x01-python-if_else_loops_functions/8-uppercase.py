#!/usr/bin/python3
low = "abdcdefghijklmnopqrstqwxyz"
upp = "ABCDEFGHIJKLMNOPQRSTQWXYZ"
def uppercase(str):
    new_str = ""
    for i in range(len(str)):
        for j in range(len(low)):
            if str[i] == low[j]:
                new_str += upp[j]
                break
        else:
            new_str += str[i]

    return print(new_str)
