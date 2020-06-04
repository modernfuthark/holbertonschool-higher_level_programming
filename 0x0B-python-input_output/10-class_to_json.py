#!/usr/bin/python3
""" 10-class_to_json: Convert a class to a json file """


def class_to_json(obj):
    """ class_to_json: Returns a dictionary of an obj """
    if hasattr(obj, "__dict__"):
        return obj.__dict__
