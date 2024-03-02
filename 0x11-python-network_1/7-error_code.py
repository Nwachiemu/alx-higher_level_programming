#!/usr/bin/python3
"""script that takes in a URL, sends a request
to the URL and displays the body of the response."""


if __name__ == '__main__':
    from sys import argv
    from requests import get

    Link = argv[1]
    ask = get(Link)
    ERR_TXT = 'Error code: {}'
    status = ask.status_code
    print(ERR_TXT.format(status) if (status >= 400) else ask.text)
