#!/usr/bin/python3
""" 6-from_json_string: Return an object from a JSON string """
import json


def from_json_string(my_str):
    """ from_json_string: Return an obj from my_str """
    return json.loads(my_str)
