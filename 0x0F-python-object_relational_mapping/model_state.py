#!/usr/bin/python3
""" Define the State model """
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class State(Base):
    """ This defines a class state to be linked to db table """
    __tablename__ = 'states'

    id = Column(Integer, nullable=False,
                autoincrement=True, unique=True,
                primary_key=True)

    name = Column(String(128), nullable=False)
