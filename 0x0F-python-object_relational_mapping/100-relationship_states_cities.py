#!/usr/bin/python3

"""
a script that creates the State “California” with
the City “San Francisco” from the database hbtn_0e_100_usa.
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

    california = State(name="California")
    san_francisco = City(name="San Francisco", state=california)
    california.cities.append(san_francisco)

    session.add(california)
    session.add(san_francisco)

    session.commit()

    session.close()
