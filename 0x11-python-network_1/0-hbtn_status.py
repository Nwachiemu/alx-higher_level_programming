#!/usr/bin/python3
"""script that fetches https://alx-intranet.hbtn.io/status"""
import urllib.request


if __name__ == "__main__":
    ask = urllib.request.Request("https://alx-intranet.hbtn.io/status")
    with urllib.request.urlopen(ask) as response:
        content = response.read()

        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
        print("\t- utf8 content: {}".format(content.decode("utf-8")))
