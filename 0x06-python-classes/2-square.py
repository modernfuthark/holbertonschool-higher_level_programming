#!/usr/bin/python3
""" 2-square: File for the Square class"""


class Square:
    """Square: Square class"""
    def __init__(self, size=0):
        """__init__: Init method"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
