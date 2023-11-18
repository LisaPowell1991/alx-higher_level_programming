#!/usr/bin/python3

"""
A script that  lists all State objects that
contain the letter a from the database hbtn_0e_6_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db = sys.argv[3]

    engine = create_engine(
            f'mysql://{username}:{password}@localhost:3306/{db}')

    Base.metadata.bind = engine

    DBsession = sessionmaker(bind=engine)
    session = DBsession()

    new_state = State(name="Loisiana")
    session.add(new_state)
    session.commit()

    print(new_state.id)

    session.close()
