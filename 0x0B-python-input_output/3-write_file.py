#!/usr/bin/python3
""" 3-write_file: Write to a file """


def write_file(filename="", text=""):
    """ write_file: Write text into filename """
    with open(filename, 'w') as f:
        return f.write(text)
