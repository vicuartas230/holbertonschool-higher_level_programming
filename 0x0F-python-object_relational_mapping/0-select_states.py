#!/usr/bin/python3
""" This script lists all states from the database hbtn_0e_0_usa. """
import MySQLdb
from sys import argv


if __name__ == '__main__':
    db = MySQLdb.connect("localhost", argv[1], argv[2], argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    for state in cursor.fetchall():
        print(state)
    db.close()
