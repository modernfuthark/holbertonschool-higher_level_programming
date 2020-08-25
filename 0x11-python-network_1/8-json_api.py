#!/usr/bin/python3
""" 8-json_api: Sends a post request to a set url """

import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) > 1:
        inp = sys.argv[1]
    else:
        inp = ""

    data = {'q': inp}
    url = "http://0.0.0.0:5000/search_user"

    req = requests.post(url, data)

    try:
        req = req.json()

        if req:
            print("[{}] {}".format(req.get("id"), req.get("name")))
        else:
            print("No Result")
    except ValueError:
        print("Not a valid JSON")
