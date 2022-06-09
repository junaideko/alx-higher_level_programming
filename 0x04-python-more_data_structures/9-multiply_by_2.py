#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    newDict = a_dictionary.copy()
    for k, v in a_dictionary.items():
        newDict[k] = v * 2
    return newDict
