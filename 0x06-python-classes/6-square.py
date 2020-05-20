#!/usr/bin/python3
""" 6-square: File for the Square class"""


class Square:
    """Square: Square class"""
    def __init__(self, size=0, position=(0, 0)):
        """__init__: Init method"""
        self.sizeset(size)
        self.position_set(position)

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
            raise ValueError("size must be >= 0")
        self.__size = newsize

    def my_print(self):
        """my_print: Print the square"""
        if self.__size == 0:
            print("")
        else:
            print("\n" * self.__position[1], end="")
            for i in range(0, self.__size):
                print(" " * self.__position[0], end="")
                for j in range(0, self.__size):
                    print("#", end="")
                print("")

    def position_set(self, newpos):
        """position_set: Set position"""
        if type(newpos) != tuple or len(newpos) < 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(newpos[0]) != int or type(newpos[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if newpos[0] < 0 or newpos[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = newpos

    def position_get(self):
        """position_get: Get position"""
        return self.__position

    position = property(position_get, position_set)
    size = property(sizeget, sizeset)
