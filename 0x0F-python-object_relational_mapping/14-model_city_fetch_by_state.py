#!/usr/bin/python3
"""
    Script that prints all City objects and their associated State names
    from the database hbtn_0e_14_usa.

    The script performs the following:
    - Joins the State and City tables based on their relationship.
    - Orders the results by City.id.
    - Outputs each City object in the format: <state_name>: (<city_id>) <city_name>.
"""
import sys
from model_state import Base, State
from model_city import City

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sqlalchemy import asc


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    start = sessionmaker()
    start.configure(bind=engine)

    session = start()
    stmt = session.query(State, City).join(City).order_by(asc(City.id)).all()
    for i, j in stmt:
        print("{:s}: ({:d}) {:s}".format(i.name, j.id, j.name))

    session.close()
