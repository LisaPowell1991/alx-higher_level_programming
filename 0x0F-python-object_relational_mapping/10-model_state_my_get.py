#!/usr/bin/python3

"""
A script that prints the first State object
from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db = sys.argv[3]
    state_name = sys.argv[4]

    engine = create_engine(
            f'mysql://{username}:{password}@localhost:3306/{db}')

    Base.metadata.bind = engine

    DBsession = sessionmaker(bind=engine)
    session = DBsession()

    state_result = session.query(State).filter_by(name=state_name).first()

    if state_result:
        print(state_result.id)
    else:
        print("Not found")

    session.close()
