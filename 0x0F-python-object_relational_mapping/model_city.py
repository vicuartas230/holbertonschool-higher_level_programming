#!/usr/bin/python3
""" This script contains the class definition of a City. """
from model_state import Base, State
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey

Base = declarative_base()


class City(Base):
    """ This class inheritances of Base class """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)

    def __init__(self, name):
        self.name = name
