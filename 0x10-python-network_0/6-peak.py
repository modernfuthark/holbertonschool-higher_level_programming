#!/usr/bin/python3
""" 6-peak: Find the peak of a list """


def find_peak(list_of_integers):
    """ Finds the peak of a list """
    if len(list_of_integers) is 0:
        return None
    peak = list_of_integers[0]

    for i in range(1, len(list_of_integers)):
        if list_of_integers[i - 1] < list_of_integers[i]:
            if list_of_integers[i + 1] < list_of_integers[i]:
                peak = list_of_integers[i]
    return peak
