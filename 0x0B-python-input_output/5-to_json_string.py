#!/usr/bin/python3
""" 5-to_json_string: Return an object's JSON data """
import json


def to_json_string(my_obj):
    """ to_json_string: Return the JSON representation of an object """
    return json.dumps(my_obj)
