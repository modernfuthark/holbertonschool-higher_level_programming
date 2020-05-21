#!/usr/bin/python3
""" 0-add_integer: Adds 2 ints """


def add_integer(a, b=98):
    """ add_integer: Add 2 ints, a & b, return the sum """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
