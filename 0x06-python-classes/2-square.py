#!/usr/bin/python3
"""module write a class square"""


class Square:
    """Repersent a square class """

    def __init__(self, size=0):
        """ define and initialize an attribute size

        Args:
        size (int): size of square initailized to zero
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
