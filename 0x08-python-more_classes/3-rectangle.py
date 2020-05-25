#!/usr/bin/python3
""" 3-rectangle: File for the Rectangle class """


class Rectangle:
    """ Rectangle class """
    def __init__(self, width=0, height=0):
        """ init method """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """ Width getter """
        return self.__width

    @width.setter
    def width(self, value):
        """ Width setter """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Height getter """
        return self.__height

    @height.setter
    def height(self, value):
        """ Height setter """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Returns the area of the rectangle """
        return self.__width * self.__height

    def perimeter(self):
        """ Returns the perimeter of the rectangle """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """ String representation """
        rec = ""
        for i in range(0, self.__height):
            rec += ('#' * self.width)
            if i != self.__height - 1:
                rec += "\n"
        return rec
