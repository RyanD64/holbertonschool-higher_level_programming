#!/usr/bin/python3
"""contains the class definition of a state"""

import sqlalchemy
from sqlalchemy import Integer,Column,String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """class State"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
