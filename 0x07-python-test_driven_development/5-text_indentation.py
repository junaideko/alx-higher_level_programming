#!/usr/bin/python3
""" Module ident text with two new lines"""


def text_indentation(text):
    """function print text with two new lines after , . ? and : character
       Args:
           text(str): text to be idented
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    for ch in text:
        if ch == "." or ch == "," or ch == "?" or ch == ":":
            print("\n")
        else:
            print(ch, end="")
