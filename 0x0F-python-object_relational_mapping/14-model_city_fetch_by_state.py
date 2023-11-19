#!/usr/bin/python3

"""
A script that prints all City objects from the database hbtn_0e_14_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db = sys.argv[3]

    engine = create_engine(
            f'mysql://{username}:{password}@localhost:3306/{db}')

    Base.metadata.bind = engine

    DBsession = sessionmaker(bind=engine)
    session = DBsession()

    cities =
    session.query(City).order_by(City.state_id, City.id, City.id).all()

    for city in cities:
        state = session.query(State).filter_by(
                id=city.state_id).first()
        print(f"{state.name}: ({city.id}) {city.name}")

    session.close()
