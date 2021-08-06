#!/usr/bin/python
""" This script lists all cities from the database hbtn_0e_4_usa. """
import MySQLdb
from sys import argv


if __name__ == '__main__':
    db = MySQLdb.connect("localhost", argv[1], "Root#10.", argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT cities.id, cities.name, states.name FROM cities \
INNER JOIN states ON cities.state_id=states.id ORDER BY cities.id")
    for state in cursor.fetchall():
        print(state)
    db.close()
