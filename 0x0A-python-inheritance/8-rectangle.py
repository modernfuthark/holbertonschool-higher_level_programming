#!/usr/bin/python3
""" 8-rectangle: File for the Rectangle class """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectangle: Rectangle class """

    def __init__(self, width, height):
        """ __init__: Initial method """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
