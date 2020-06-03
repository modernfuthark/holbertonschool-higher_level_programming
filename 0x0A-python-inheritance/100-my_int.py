#!/usr/bin/python3
""" 100-my_int: Rebellious int """


class MyInt(int):
    """ MyInt: A rebellious int """
    def __eq__(self, other):
        """ __eq__: Equals """
        return super().__ne__(other)

    def __ne__(self, other):
        """ __ne__: Not equals """
        return super().__eq__(other)
