#!/usr/bin/python3
""" 8-json_api: Sends a post request to a set url """

import requests
import sys


if __name__ == "__main__":
    inp = ""
    if len(sys.argv) > 1:
        inp = sys.argv[1]

    data = {'q': inp}
    url = "http://0.0.0.0:5000/search_user"

    req = requests.post(url, data)

    id = req.json().get("id")
    name = req.json().get("name")

    if id is not None and name is not None:
        print("[{}] {}".format(id, name))
    else:
        print("No result")
