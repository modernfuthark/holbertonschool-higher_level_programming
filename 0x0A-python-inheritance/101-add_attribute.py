#!/usr/bin/python3
""" 101-add_attribute: Add an attribute to a class """

class Empty:
    """ Empty class """
    pass

def add_attribute(obj, name, val):
    """ add_attribute: Adds an attribute to obj """
    tester = Empty()
    if type(obj) is not type(tester):
        raise TypeError("can't add new attribute")
    setattr(obj, name, val)
