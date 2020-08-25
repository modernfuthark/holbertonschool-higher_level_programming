#!/usr/bin/python3
""" 4-hbtn_status: gets status using requests rather than urllib """

import requests


if __name__ == "__main__":
    req = requests.get("https://intranet.hbtn.io/status")
    print("Body responce:")
    print("\t- type: {}".format(type(req.text)))
    print("\t- content: {}".format(req.text))
