#!/usr/bin/python
""" This script takes in an argument and displays all values in
    the states table of hbtn_0e_0_usa where name matches the argument. """
import MySQLdb
from sys import argv


if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost\
",user=argv[1], passwd=argv[2], db=argv[3])
    cursor = db.cursor()
    query = "SELECT * FROM states \
WHERE name='{}' ORDER BY id ASC".format(argv[4])
    cursor.execute(query)
    for state in cursor.fetchall():
        print(state)
    db.close()
