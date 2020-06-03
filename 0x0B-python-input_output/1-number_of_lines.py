#!/usr/bin/python3
""" 1-number_of_lines: Returns the number of lines in a file """


def number_of_lines(filename=""):
    """ number_of_lines: Return num of lines in filename """
    lines = 0
    with open(filename, 'r') as f:
        for i in f:
            lines += 1
    return lines
