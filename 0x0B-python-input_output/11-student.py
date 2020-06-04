#!/usr/bin/python3
""" 11-student: File for the Student class """


class Student:
    """ Student class """

    def __init__(self, first_name, last_name, age):
        """ __init__: Initital method """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ to_json: Returns the dictionary of self """
        return self.__dict__
