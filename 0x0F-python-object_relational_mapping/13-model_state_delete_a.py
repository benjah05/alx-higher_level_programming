#!/usr/bin/python3
"""SQLAlchemy"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sqlalchemy import asc

if __name__ == "__main__":
    """ delete all states containing 'a' """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    start = sessionmaker()
    start.configure(bind=engine)
    session = start()
    filter_query = State.delete().where(State.name.like("%a%"))
    result = filter_query.all()
    for i in result:
        session.delete(i)
    session.commit()

    session.close()
