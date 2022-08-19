#!/usr/bin/python3
"""python script that fetche an url"""


if __name__ == "__main__":
    import requests
    import sys

    resp = requests.get(sys.argv[1])
    if resp.status_code:
        print("Error code: {}".format(resp.status_code))
    else:
        print(resp.text)
