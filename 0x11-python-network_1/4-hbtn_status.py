#!/usr/bin/python3
"""python script that fetche an url"""


if __name__ == "__main__":
    import requests

    url = requests.get("https://intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(url.text)))
    print("\t- content: {}".format(url.text))
