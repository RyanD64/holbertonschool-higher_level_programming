#!/usr/bin/python3
"""contains the class definition of a city"""

from sqlalchemy import Integer, Column, ForeignKey,String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """class City"""
    __tablename__ = 'cities'
    id = Column(Integer, autoincrement=True ,primary_key=True, nullable=False, unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
