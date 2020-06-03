#!/usr/bin/python3
""" 4-inherits_from: Returns true if obj is an instance of class """


def inherits_from(obj, a_class):
    """ inherits_from: Checks if obj inherits from a_class """
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    return False
