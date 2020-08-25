#!/usr/bin/python3
""" 6-post_email: gets an email from a url aaaaaaaaaaaaaa """

import requests
import sys


if __name__ == "__main__":
    info = {'email': sys.argv[2]}
    req = requests.post(sys.argv[1], info)
    print(req.text)
