#!/usr/bin/python3
""" 4-square: File for the Square class"""


class Square:
    """Square: Square class"""
    def __init__(self, size=0):
        """__init__: Init method"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """area: Return the area of the square"""
        return self.__size * self.__size

    def sizeget(self):
        """sizeget: Get the size of class"""
        return self.__size

    def sizeset(self, newsize=0):
        """sizeset: Set size of object"""
        if type(newsize) != int:
            raise TypeError("size must be an integer")
        if newsize < 0:
            raise ValueError("size mustbe >= 0")

        self.__size = newsize
    size = property(sizeget, sizeset)
