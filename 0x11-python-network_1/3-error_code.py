#!/usr/bin/python3
"""python script that fetche an url"""


if __name__ == "__main__":
    import urllib.request
    from urllib.error import HTTPError
    from sys import argv

    try:
        with urllib.request.urlopen(argv[1]) as response:
            print(response.read().decode('utf-8'))
    except HTTPError as response:
        print("Error code: {]".format(response.code))
