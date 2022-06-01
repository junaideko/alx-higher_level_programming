#!/usr/bin/python3
"""prints upper case , else convers lower case to uppercas"""
def uppercase(str):
    for ch in str:
        if 97 <= ord(ch) <= 122:
            ch = chr(ord(ch) - 32)
        print("{}".format(ch), end="")
    print("")
