#!/usr/bin/python3
"""
script that takes in a URL, sends a request to the URL and
displays the body of the response (decoded in utf-8).
"""


import sys
from urllib import request, error


if __name__ == '__main__':
    argv = sys.argv
    Link = argv[1]
    try:
        with request.urlopen(Link) as response:
            print(response.read().decode('utf-8'))
    except error.HTTPError as ex:
        print("Error code: {}".format(ex.status))
