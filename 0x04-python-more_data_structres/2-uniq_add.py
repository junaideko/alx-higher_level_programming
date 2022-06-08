#!/usr/bin/python3
def uniq_add(my_list=[]):
    myNewList = set(my_list)
    adds = 0
    for num in myNewList:
        adds += num
    return adds
