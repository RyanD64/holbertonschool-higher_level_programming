#!/usr/bin/python3
"""python script that fetche an url"""


if __name__ == "__main__":
    import urllib.request
    import urllib.parse
    from sys import argv

    mail = {'mail': argv[2]}
    val = urllib.parse.urlencode(mail).encode('ascii')
    post = urllib.request.Request(argv[1], val)
    with urllib.request.urlopen(post) as response:
        print(response.read().decode('utf-8'))
