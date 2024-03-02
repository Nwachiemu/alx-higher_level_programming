#!/usr/bin/python3
"""
script that fetches https://alx-intranet.hbtn.io/status
"""
import requests


if __name__ == "__main__":
    ask = requests.get('https://alx-intranet.hbtn.io/status')
    t = ask.text
    print('Body response:\n\t- type: {}\n\t- content: {}'.format(type(t), t))
