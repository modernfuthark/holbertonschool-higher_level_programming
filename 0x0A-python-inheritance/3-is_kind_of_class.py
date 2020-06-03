#!/usr/bin/python3
""" 3-is_kind_of_class: Returns true if obj is a class """


def is_kind_of_class(obj, a_class):
    """ is_kind_of_class: Returns true if obj is instant of a_class """
    if isinstance(obj, a_class):
        return True
    return False
