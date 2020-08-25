#!/usr/bin/python3
""" 0-hbtn_status: Uses URLlib to request status """

import urllib.request


def main():
    """ Requests the status from a url """
    with urllib.request.urlopen("https://intranet.hbtn.io/status") as opened:
        _read = opened.read()
        print("Body response:")
        print("\t- type: {}".format(type(_read)))
        print("\t- content: {}".format(_read))
        print("\t- utf8 content: {}".format(_read.decode("utf-8")))

if __name__ == "__main__":
    main()
