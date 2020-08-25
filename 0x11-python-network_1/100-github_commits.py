#!/usr/bin/python3
""" 100-github_commits.py: Gets the 10 recent commits from a user in a repo """

import requests
import sys

if __name__ == "__main__":
    repository = sys.argv[1]
    username = sys.argv[2]

    url = "https://api.github.com/repos/{}/{}/commits?per_page=10"\
        .format(username, repository)
    # print(url)

    req = requests.get(url)
    req = req.json()

    # print(req)
    for com in req:
        # print(com)
        sha = com.get("sha")
        name = com.get("commit").get("author").get("name")
        print("{}: {}".format(sha, name))
