#!/usr/bin/python3
""" This script prints the first State object
    from the database hbtn_0e_6_usa. """
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session, sessionmaker


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}\
'.format('root', 'Root#10.', 'hbtn_0e_6_usa'), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    consult = session.query(State).first()
    if consult:
        print("{}: {}".format(consult.id, consult.name))
    else:
        print('Nothing')
