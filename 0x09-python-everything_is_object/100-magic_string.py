#!/usr/bin/python3
def magic_string(magic=[0]):
    magic[0] += 1
    return ("Holberton, " * magic[0])[0:len("Holberton, " * magic[0]) - 2]
