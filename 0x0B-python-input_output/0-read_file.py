#!/usr/bin/python3
""" 0-read_file: Read a file """


def read_file(filename=""):
    with open(filename) as f:
        readtext = f.read())
    print(readtext, end="")
