#!/usr/bin/python3
"""python script that fetche an url"""


if __name__ == "__main__":
    import urllib.request
    from sys import argv

    with urllib.request.urlopen(argv[1]) as response:
        url = response.headers.get('X-Request-Id')
        print(url)
