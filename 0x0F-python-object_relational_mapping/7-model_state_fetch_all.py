#!/usr/bin/python3
""" This script lists all State objects from the database hbtn_0e_6_usa. """
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}\
'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    query = engine.execute("SELECT * FROM states ORDER BY id ASC")
    for state in query:
        print("{}: {}".format(state[0], state[1]))
