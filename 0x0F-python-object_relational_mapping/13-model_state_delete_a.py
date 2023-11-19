#!/usr/bin/python3

"""
A script that deletes all State objects with a name
containing the letter 'a' from the database hbtn_0e_6_usa.
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
            f'mysql://{username}:{password}@localhost:3306/{db}',
            pool_pre_ping=True)

    DBsession = sessionmaker(bind=engine)
    session = DBsession()

    states_to_delete = session.query(State).filter(
            State.name.like('%a%')).all()

    for state in states_to_delete:
        session.delete(state)

    session.commit()

    session.close()
