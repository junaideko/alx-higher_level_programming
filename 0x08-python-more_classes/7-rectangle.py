#!/usr/bin/python3
"""module defines a rectangle by width, height, area,
and perimeter
"""


class Rectangle:
    """class representation of a rectangle, c
    :cvar number_of_instnaecs - count the num of instances
    :cvar print_symbol - symbol for string representation
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ initializes a rectangle
        Args:
            width(int): width of rectangle set to 0
            height(int): height of rectagle set to 0
        """

        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """get and return width of rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """set width with value and return nothing"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >=0")
        self.__width = value

    @property
    def height(self):
        """get and return height of rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """set height with value and return nothing"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >=0")
        self.__height = value

    def area(self):
        """public instance method the returns area"""
        return (self.__width * self.__height)

    def perimeter(self):
        """public instance method the returns perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return((self.__width + self.__height) * 2)

    def __str__(self):
        """define the string representation of rectabgle"""
        if self.__width == 0 or self.__height == 0:
            return ""
        rect = []
        for i in range(self.__height):
            for j in range(self.__width):
                rect.append("#")
            if i != self.__height - 1:
                rect.append("\n")
        return "".join(rect)

    def __repr__(self):
        """return a string representation of rec"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """prints a message when a rectangle obj is deleted
        and decrements number of instances of rectangle
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
