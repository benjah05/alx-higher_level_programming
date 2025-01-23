#!/usr/bin/python3
"""SQLAlchemy"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sqlalchemy import asc

if __name__ == "__main__":
    """First State"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    start = sessionmaker()
    start.configure(bind=engine)
    session = start()
    filter_query = session.query(State).order_by(asc(State.id)).first()
    if filter_query:
        print("{:d}: {:s}".format(filter_query.id, filter_query.name))
    else:
        print("Nothing")

    session.close()
