#!/usr/bin/python3
"""4-print_suare module prints a square with the character #"""


def print_square(size):
    """print_square method print a square with the character #
       Args:
           size(int): is the size length of the square and must be an int.
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
