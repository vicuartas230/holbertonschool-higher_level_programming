#!/usr/bin/python
""" This script lists all states from the database hbtn_0e_0_usa. """
import MySQLdb
from sys import argv


if __name__ == '__main__':
    db = MySQLdb.connect("localhost", argv[1], "Root#10.", argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    a = cursor.fetchone()
    # while a:
    #     print(a)
    #     a = cursor.fetchone()
    for state in a:
        print(state)
    db.close()
