#!/usr/bin/python3
"""A subclass of class BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class Rectangle that inherits from BaseGeometry
    Subclass is initialized with args
    Args:
        width (int): width of the subclass Rectangle
        height (int): heigth of the subclass Rectangle
    """

    def __init__(self, width, height):

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        """String representatin of area value"""
        # return "[Rectangle] {:d}/{:d}"
        # .format(self.__width, self.__height), end=""
        print("[Rectangle] {:d}/{:d}"
              .format(self.__width, self.__height), end="")
        return ""
