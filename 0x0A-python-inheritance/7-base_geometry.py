#!/usr/bin/python3
""" 7-base_geometry: Creates an empty class BaseGeometry """


class BaseGeometry:
    """ BaseGeometry: Empty class """

    def area(self):
        """ area: Does nothing at the moment """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ integer_validator: Validates value """
        if type(value) is not int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")
