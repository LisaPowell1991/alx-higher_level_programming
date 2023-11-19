#!/usr/bin/python3

"""
A python file that contains the class definition
of a State and an instance Base = declarative_base().
"""

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """
    Represents a state in a MySQL database.

    Attribute:
    id (int): Auto-generated, unique int acting as primary key.
    name (str): String representing the name of the state.
    """

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")
