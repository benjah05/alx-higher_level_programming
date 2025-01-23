#!/usr/bin/python3
"""
    python file that contains the class definition
    of a State and an instance Base = declarative_base()
"""
import sys
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
Base = declarative_base()
"""Instance"""


class State(Base):
    """
    Class State that inherits from Base
    args:
        __tablename__: the name of the table
        id: id column (primary key)
        name: name column
        engine: establish the connection with CL arguments
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
