#!/usr/bin/python3
"""python script that fetche an url"""


if __name__ == "__main__":
    import requests
    import sys

    url = requests.post(sys.argv[1], data={"email": sys.argv[2]})
    print(url.text)
