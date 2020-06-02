#!/usr/bin/python3
""" 1-is_same_class: Return true or false if a class is the same """


def is_same_class(obj, a_class):
    """ is_same_class: Return true or false is a class is the same """
    if type(obj) is a_class:
        return True
    return False
