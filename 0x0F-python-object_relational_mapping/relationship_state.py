#!/usr/bin/python3
""" Define the State model """
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """ Define class State to be linked to db table """
    __tablename__ = 'states'

    id = Column(Integer, nullable=False,
                autoincrement=True, unique=True,
                primary_key=True)

    name = Column(String(128), nullable=False)

    cities = relationship('City', cascade='all, delete', backref='state')
