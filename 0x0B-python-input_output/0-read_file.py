#!/usr/bin/python3
""" 0-read_file: Read a file """


def read_file(filename=""):
    """ read_file: Reads a file """
    with open(filename) as f:
        print(f.read(), end="")
