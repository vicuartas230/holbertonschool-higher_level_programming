#!/usr/bin/python3
""" This script lists all State objects that contain
    the letter a from the database hbtn_0e_6_usa. """
import sys
from sqlalchemy.sql.expression import desc
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session, sessionmaker


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}\
'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    consult = session.query(State).filter(State.name.ilike('%a%\
')).order_by(State.id).all()
    for state in consult:
        print("{}: {}".format(state.id, state.name))
