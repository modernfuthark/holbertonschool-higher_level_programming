#!/usr/bin/python3
""" 5-hbtn_header: gets the x-request-id using requests """

import requests
import sys


if __name__ == "__main__":
    req = requests.get(sys.argv[1])
    print(req.headers.get("X-Request-Id"))
