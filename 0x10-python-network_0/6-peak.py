#!/usr/bin/python3
""" 6-peak: Find the peak of a list """


def find_peak(list_of_integers):
    """ Finds the peak of a list """
    listlen = len(list_of_integers)
    if listlen is 0:
        return None
    end = search(0, list_of_integers, listlen - 1)
    return list_of_integers[end]


def search(low, _list, high):
    """ Recursive peak search using high and low """
    if low >= high:
        return low

    test = ((high - low) // 2) + low

    if _list[test] > _list[test + 1]:
        return search(low, _list, test)
    else:
        return search(test + 1, _list, high)
