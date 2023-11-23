#!/usr/bin/python3

"""
A script that lists all City objects from the database hbtn_0e_101_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db = sys.argv[3]

    engine = create_engine(
            f'mysql+mysqldb://{username}:{password}@localhost:3306/{db}')

    Base.metadata.create_all(engine)

    DBsession = sessionmaker(bind=engine)
    session = DBsession()

    cities = session.query(City).order_by(City.id).all()

    for city in cities:
        print(f'{city.id}: {city.name} -> {city.state.name}')

    session.close()
