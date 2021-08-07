#!/usr/bin/python3
""" This script contains the class definition of a State
    and an instance Base = declarative_base() """
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    """ This class inheritances of Base class """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    name = Column(String(128), nullable=False)

    def __init__(self, name):
        self.name = name
