#!/usr/bin/python3
""" 4-append_write: Append to the end of a file """


def append_write(filename="", text=""):
    """ append_write: Append text onto filename """
    with open(filename, 'a') as f:
        return f.write(text)
