#!/usr/bin/python3
""" 4-print_square: prints a square """


def print_square(size):
    """ print_square: print a square of size 'size' """

    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    if size is 0:
        print("")
        return
    for i in range(0, size):
        print('#' * size)
