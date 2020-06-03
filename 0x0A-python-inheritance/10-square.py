#!/usr/bin/python3
""" 10-square: File for the Square class """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Square: A square class """

    def __init__(self, size):
        """ __init__: Initial method """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """ area: Return the area """
        return self.__size * self.__size

    def __str__(self):
        """ __str__: String implementation """
        return "[Rectangle] {}/{}".format(self.__size, self.__size)
