#!/usr/bin/python3
"""script in python that list all states from a database"""

from sys import argv
import MySQLdb

if __name__ == '__main__':
    start = MySQLdb.connect(host="localhost", port=3306,
                            user=argv[1], passwd=argv[2],
                            db=argv[3], charset="utf8")

    go = start.cursor()
    go.execute("SELECT cities.name FROM cities JOIN states ON \
                cities.state_id = states.id WHERE states.name LIKE %s \
                ORDER BY cities.id", (argv[4], ))
    rows = go.fetchall()
    print(", ".join(row[0] for row in rows))
    go.close()
    start.close()
