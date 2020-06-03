#!/usr/bin/python3
""" 9-rectangle: File for the Rectangle class """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectangle: Rectangle class """

    def __init__(self, width, height):
        """ __init__: Initial method """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """ area: Return the area of the Rectangle """
        return self.__width * self.__height

    def __str__(self):
        """ __str__: Return a string of info """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
