#!/usr/bin/python3
""" 8-load_from_json_file: Create an object from a json file """
import json


def load_from_json_file(filename):
    """ load_from_json_file: Create an object fromm a json file """
    with open(filename, 'r') as f:
        return json.loads(f.read())
