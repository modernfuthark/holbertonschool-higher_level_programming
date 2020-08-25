#!/usr/bin/python3
""" 1-hbtn_header: Sends a request to a url """

import urllib.request
import sys


def main():
    """ Gets the X-Request-Id from a url """
    with urllib.request.urlopen(sys.argv[1]) as opened:
        _read = opened.info()
        print(_read.get("X-Request-Id"))

if __name__ == "__main__":
    main()
