#!/usr/bin/python3
""" This script lists all State objects, and corresponding City
objects, contained in the database hbtn_0e_101_usa. """
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session, sessionmaker
from relationship_state import State, Base
from relationship_city import City
import sys

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}\
'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    consult = session.query(State).all()
    for state in consult:
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
                print("\t{}: {}".format(city.id, city.name))
