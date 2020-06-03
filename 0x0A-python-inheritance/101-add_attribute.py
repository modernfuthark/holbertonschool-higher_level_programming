#!/usr/bin/python3
""" 101-add_attribute: Add an attribute to a class """


def add_attribute(obj, name, val):
    if isinstance(obj, type) is False:
        raise TypeError("can't add new attribute")
    setattr(obj, name, val)
