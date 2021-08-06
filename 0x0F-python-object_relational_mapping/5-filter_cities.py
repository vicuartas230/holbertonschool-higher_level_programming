#!/usr/bin/python
""" This script lists all cities from the database hbtn_0e_4_usa. """
import MySQLdb
from sys import argv


if __name__ == '__main__':
    db = MySQLdb.connect("localhost", argv[1], "Root#10.", argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT cities.name FROM cities INNER JOIN states ON \
cities.state_id=states.id WHERE states.name=%s ORDER BY \
cities.id;", (argv[4],))
    tupl = cursor.fetchall()
    for state in tupl:
        print("{}".format(state[0]))
    db.close()
