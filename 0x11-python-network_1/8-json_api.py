#!/usr/bin/python3
""" script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
Sends a request to the URL and displays the body of the response."""


if __name__ == '__main__':
    from requests import post
    from sys import argv

    URL = 'http://0.0.0.0:5000/search_user'
    data = {'q': argv[1] if len(argv) >= 2 else ""}
    ask = post(URL, data)

    type_res = ask.headers['content-type']

    if type_res == 'application/json':
        answer = ask.json()
        _id = answer.get('id')
        name = answer.get('name')
        if (answer != {} and _id and name):
            print("[{}] {}".format(_id, name))
        else:
            print('No result')
    else:
        print('Not a valid JSON')
