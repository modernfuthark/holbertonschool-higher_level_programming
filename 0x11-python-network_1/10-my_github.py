#!/usr/bin/python3
""" 10-my_github: use the GitHub API to print an ID """

import requests
import sys


if __name__ == "__main__":
    url = "https://api.github.com/user"

    usrnm = sys.argv[1]
    psswd = sys.argv[2]

    session = requests.Session()
    session.auth = (usrnm, psswd)

    print(session.get(url).json().get("id"))
