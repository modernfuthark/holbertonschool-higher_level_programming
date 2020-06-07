#!/usr/bin/python3
""" rectangle: File for the Rectangle class """
from models.base import Base


class Rectangle(Base):
    """ Rectangle: Rectangle class """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ __init__: Initial method """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ Getter """
        return self.__width

    @width.setter
    def width(self, width):
        """ Setter """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """ Getter """
        return self.__height

    @height.setter
    def height(self, height):
        """ Setter """
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """ Getter """
        return self.__x

    @x.setter
    def x(self, x):
        """ Setter """
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """ Getter """
        return self.__y

    @y.setter
    def y(self, y):
        """ Setter """
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """ Return the area of the rectangle """
        return self.__width * self.__height

    def display(self):
        """ Display the rectangle """
        print("\n" * self.__y, end="")
        for i in range(0, self.__height):
            print(" " * self.__x, end="")
            print("#" * self.__width)

    def __str__(self):
        """ __str__: String override """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args):
        """ update: Update the rectangle """
        if len(args) is not 0:
            arglength = len(args)
            if arglength >= 1:
                self.id = args[0]
            if arglength >= 2:
                self.__width = args[1]
            if arglength >= 3:
                self.__height = args[2]
            if arglength >= 4:
                self.__x = args[3]
            if arglength >= 5:
                self.__y = args[4]
