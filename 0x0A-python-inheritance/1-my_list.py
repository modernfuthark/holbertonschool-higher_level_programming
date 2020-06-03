#!/usr/bin/python3
""" 1-my_list: Creates a class MyList """


class MyList(list):
    """ MyList: List class """
    def print_sorted(self):
        """ print_sorted: Prints self sorted in ascending order """
        print(sorted(self))
