#!/usr/bin/python3
""" 13-student: File for the Student class """


class Student:
    """ Student class """

    def __init__(self, first_name, last_name, age):
        """ __init__: Initital method """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ to_json: Returns the dictionary of self """
        if attrs is None or type(attrs) != list:
            return self.__dict__

        new = {}
        for element in attrs:
            if type(element) is not str:
                return self.__dict__
            try:
                new[element] = getattr(self, element)
            except:
                pass
        return new

    def reload_from_json(self, json):
        """ reload_from_json: Replace all attrs of Student """
        for key in json:
            setattr(self, key, json[key])
