#!/usr/bin/python3
def search_replace(my_list, search, replace):
    newList = []
    for num in my_list:
        if num == search:
            num = replace
        newList.append(num)
    return newList
