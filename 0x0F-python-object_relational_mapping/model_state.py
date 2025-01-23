#!/usr/bin/python3
"""First class model"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

# Define Base here
Base = declarative_base()


class State(Base):
    """Class City that inherits from Base"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
