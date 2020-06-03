#!/usr/bin/python3
""" 101-add_attribute: Add an attribute to a class """


def add_attribute(obj, name, val):
    """ add_attribute: Adds an attribute to obj """
    if isinstance(obj, type) is False:
        raise TypeError("can't add new attribute")
        return
    if hasattr(obj, '__init__') is True:
        setattr(obj, name, val)
    else:
        raise TypeError("can't add new attribute")
