#!/usr/bin/python3
"""modules defines a class square"""


class Square:
    """represents square class"""

    def __init__(self, size=0)
    """size attribute defined and initialized

    Args:
    size (int): size of square initailed to 0
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    self.__size = size

    def area(self):
        """a public instance that return the area of square"""
        return self.__size * self.__size
