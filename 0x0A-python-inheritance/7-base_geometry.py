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
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
