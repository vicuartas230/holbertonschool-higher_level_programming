#!/usr/bin/python
""" Once again, this script takes in arguments and displays all values
    in the states table of hbtn_0e_0_usa where name matches the argument. But
    this time, this script writes one that is safe from MySQL injections! """
import MySQLdb
from sys import argv


if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost\
", user=argv[1], passwd=argv[2], db=argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name=%s", (argv[4],))
    for state in cursor.fetchall():
        print(state)
    db.close()
