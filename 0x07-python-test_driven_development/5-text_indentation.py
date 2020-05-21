#!/usr/bin/python3
""" 5-text_indentation: Split up a string """


def text_indentation(text):
    """ text_indentation: Split a string 'text' into multiple lines """
    if type(text) is not str:
        raise TypeError("text must be a string")

    nl = True
    for i in text:
        if nl is True and i is " ":
            nl = False
        else:
            print(i, end="")
            nl = False
        if i in ['.', '?', ':']:
            print("\n")
            nl = True
