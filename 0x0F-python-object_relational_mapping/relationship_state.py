#!/usr/bin/python3
"""contains the class definition of a state"""

from relationship_city import City, Base
from sqlalchemy import Integer, Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

class State(Base):
    """class State"""
    __tablename__ = 'states'
    id = Column(Integer, autoincrement=True ,primary_key=True, nullable=False, unique=True)
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state', cascade='all, delete-orphan')