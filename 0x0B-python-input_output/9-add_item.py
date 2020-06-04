#!/usr/bin/python3
""" 9-add_item: Add all arguments to a list """
import json
import sys
jsonsave = __import__('7-save_to_json_file').save_to_json_file
jsonload = __import__('8-load_from_json_file').load_from_json_file


def main():
    """ main: Main function """
    try:
        arglist = jsonload("add_item.json")
    except:
        arglist = []
    for i in range(1, len(sys.argv)):
        arglist.append(sys.argv[i])
    jsonsave(arglist, "add_item.json")

if __name__ == "__main__":
    main()
