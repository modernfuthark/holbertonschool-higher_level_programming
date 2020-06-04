#!/usr/bin/python3
""" 7-save_to_json_file: Save json string to a file """
import json


def save_to_json_file(my_obj, filename):
    """ save_to_json_file: Save obj to filename in json """
    with open(filename, 'w') as f:
        f.write(json.dumps(my_obj))
