#!/usr/bin/python3
"""SQLAlchemy"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sqlalchemy import asc

if __name__ = "__main__":
    """Get a state"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    searched_name = sys.argv[4]
    start = sessionmaker()
    start.configure(bind=engine)
    session = start()
    filter_query = session.query(State).filter(State.name == searched_name).order_by(asc(State.id)).all()
    if filter_query:
        print("{:d}".format(filter_query.id))
    else:
        print("Not found")

    session.close()
