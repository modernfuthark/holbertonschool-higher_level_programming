#!/usr/bin/python3
""" 2-read_lines: Read lines from a file """
linecount = __import__('1-number_of_lines').number_of_lines


def read_lines(filename="", nb_lines=0):
    """ read_lines: Read lines from filename nb_lines times """
    with open(filename, 'r') as f:
        if nb_lines <= 0 or nb_lines > linecount(filename):
            print(f.read(), end="")
        else:
            for i in range(0, nb_lines):
                print(f.readline(), end="")
