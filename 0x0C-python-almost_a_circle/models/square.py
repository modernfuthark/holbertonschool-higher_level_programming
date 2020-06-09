#!/usr/bin/python3
""" square: File for the Square class """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square: Square class """
    def __init__(self, size, x=0, y=0, id=None):
        """ __init__: Initial method """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ __str__: Overwrite string """
        return "[Square] ({}) {}/{} - {}".\
            format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """ size: Getter """
        return self.width

    @size.setter
    def size(self, size):
        """ size: Setter """
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """ update: Updates attrs """
        if len(args) is not 0:
            arglength = len(args)
            if arglength >= 1:
                self.id = args[0]
            if arglength >= 2:
                self.size = args[1]
            if arglength >= 3:
                self.x = args[2]
            if arglength >= 4:
                self.y = args[3]
        else:
            for key, val in kwargs.items():
                setattr(self, key, val)

    def to_dictionary(self):
        """ to_dictionary: Dictionary representation """
        todict = {}
        todict["id"] = self.id
        todict["size"] = self.width
        todict["x"] = self.x
        todict["y"] = self.y
        return todict
