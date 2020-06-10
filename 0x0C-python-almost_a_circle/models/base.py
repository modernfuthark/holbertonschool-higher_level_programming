#!/usr/bin/python3
""" base: Base class """
import json


class Base:
    """ Base: Base class """
    __nb_objects = 0

    def __init__(self, id=None):
        """ __init__: Initial method """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """ to_json_string: JSON representation """
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ save_to_file: Saves JSON string to file """
        if list_objs is None:
            list_objs = []
        temp = []  # temp list
        for i in list_objs:
            # use temp to fetch all dictionaries
            temp.append(cls.to_dictionary(i))
        jsonlist = Base.to_json_string(temp)
        # save space by using in-line if statement to name file
        fn = cls.__name__ + ".json"  # Name file based on object
        with open(fn, 'w') as f:
            f.write(jsonlist)  # write to file

    @staticmethod
    def from_json_string(json_string):
        """ from_json_string: Returns the list of JSON string """
        if json_string is None or len(json_string) is 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ create: Create an instance from a pre-made dictionary """
        # temp values to create blank instance
        newinstance = cls(1, 1, 0, 0)
        newinstance.update(**dictionary)  # update values
        return newinstance

    @classmethod
    def load_from_file(cls):
        """ load_from_file: Get list instances from a file """
        fn = cls.__name__ + ".json"
        instances = []  # empty list
        with open(fn, 'r') as f:
            data = f.read()
        jason = cls.from_json_string(data)
        # Was getting an error, used for loop instead
        for i in jason:
            instances.append(cls.create(**i))
        return instances
