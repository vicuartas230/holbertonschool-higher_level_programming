#!/usr/bin/python3
""" This script prints the first State object from the database hbtn_0e_6_usa. """
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format('root', 'Root#10.', 'hbtn_0e_6_usa'), pool_pre_ping=True)
    query = engine.execute("SELECT * FROM states ORDER BY id LIMIT 1")
    for state in query:
        print("{}: {}".format(state[0], state[1]))
