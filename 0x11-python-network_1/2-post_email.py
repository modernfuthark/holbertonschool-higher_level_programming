#!/usr/bin/python3
""" 2-post_email: Gets an email? """

import urllib.request
import sys


def main():
    """ main function """
    url = sys.argv[1]
    email = sys.argv[2]

    input = {'email': email}
    data = urllib.parse.urlencode(input)
    data = data.encode("ascii")
    request = urllib.request.Request(url, data)
    with urllib.request.urlopen(request) as opened:
        print(opened.read().decode("utf-8"))


if __name__ == "__main__":
    main()
