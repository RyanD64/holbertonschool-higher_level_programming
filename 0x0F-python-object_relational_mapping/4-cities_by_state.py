#!/usr/bin/python3
"""script in python that list all states from a database"""

from sys import argv
import MySQLdb

if __name__ == '__main__':
    start = MySQLdb.connect(host="localhost", port=3306,
                            user=argv[1], passwd=argv[2],
                            db=argv[3])

    go = start.cursor()
    go.execute("SELECT cities.id, cities.name, states.name \
                FROM cities JOIN states ON cities.state_id = \
                states.id ORDER BY cities.id ASC")
    rows = go.fetchall()
    for row in rows:
        print(row)
    go.close()
    start.close()
