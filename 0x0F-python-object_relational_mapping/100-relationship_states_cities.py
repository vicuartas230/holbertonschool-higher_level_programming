#!/usr/bin/python3
""" This script creates the State “California” with
    the City “San Francisco” from the database hbtn_0e_100_usa. """
import relationship_state
import relationship_city
import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session, sessionmaker


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format('root', 'Root#10.', 'hbtn_0e_100_usa'), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    new_state = relationship_state.State(name="California")
    # new_city = City("San Francisco")
    # new_state.cities.append(new_city)
    session.add(new_state)
    session.commit()
    session.close()
