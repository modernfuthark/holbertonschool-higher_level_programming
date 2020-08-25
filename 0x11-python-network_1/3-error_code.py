#!/usr/bin/python3
""" 3-error_code: Gets an error code from a url """

import urllib.error
import urllib.request
import sys


if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as opened:
            print(opened.read().decode("utf-8"))
    except urllib.error.URLError as error:
        print("Error code: {}".format(error.code))
