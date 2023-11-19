#!/usr/bin/python3

"""
A python file that contains the
class definition of a City.
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from model_state import Base


class City(Base):
    """
    Represents a City in a MySQL database.

    Attribute:
    id (int): Auto-generated, unique int acting as primary key.
    name (str): String representing the name of the state.
    state_id (int): represents a column of an integer,
    can’t be null and is a foreign key to states.id
    """

    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)

    state = relationship("State", back_populates="cities")
