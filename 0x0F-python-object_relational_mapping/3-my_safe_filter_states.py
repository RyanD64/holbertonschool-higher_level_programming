#!/usr/bin/python3
"""script python that list all states from a database starting with N safely"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    start = MySQLdb.connect(host="localhost", port=3306,
                            user=argv[1], passwd=argv[2],
                            db=argv[3])
    go = start.cursor()
    go.execute("SELECT * FROM states WHERE name \
                REGEXP '[:alpha:]' ORDER BY id ASC".format(argv[4]))
    rows = go.fetchall()
    for row in rows:
        if row[1] == argv[4]:
            print(row)
    go.close
    start.close
