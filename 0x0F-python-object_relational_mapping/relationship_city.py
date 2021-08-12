#!/usr/bin/python3
""" This script contains the class definition of a City. """
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class City(Base):
    """ This class inheritances of Base class """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
