#!/usr/bin/python3
"""Holberton challenge"""


if __name__ == "__main__":
    import requests
    import sys

    res = requests.get("https://api.github.com/repos/{}/{}/commits"
                       .format(sys.argv[2], sys.argv[1]))
    if res.status_code >= 400:
        print("None")
    else:
        for com in res.json()[:10]:
            print("{}: {}".format(com.get("sha"),
                                  com.get("commit")
                                     .get("author")
                                     .get("name")))
