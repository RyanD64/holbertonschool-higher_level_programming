#!/usr/bin/python3
"""python script that fetche an url"""


if __name__ == "__main__":
    import requests
    import sys

    url = requests.get(sys.argv[1])
    print(url.headers.get("X-Request-Id"))
