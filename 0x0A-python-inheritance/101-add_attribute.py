#!/usr/bin/python3
""" 101-add_attribute: Add an attribute to a class """


def add_attribute(obj, name, val):
    """ add_attribute: Adds an attribute to obj """
    if hasattr(obj, "__dict__") is False:
        raise TypeError("can't add new attribute")
    setattr(obj, name, val)
