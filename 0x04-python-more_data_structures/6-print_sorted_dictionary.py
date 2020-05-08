#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    alphabetical = sorted(a_dictionary.items(), key=lambda x: x[0])
    for i, j in alphabetical:
        print("{:s}: {}".format(i, j))
