#!/usr/bin/python3
"""lists all City objects from the database hbtn_0e_101_usa"""

from relationship_state import Base
from relationship_city import City
from sys import argv
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy.schema import Table

if __name__ == "__main__":
    eng = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                        .format(argv[1], argv[2], argv[3], pool_pre_ping=True))
    Base.metadata.create_all(eng)
    ses = Session(eng)
    for city in ses.query(City).order_by(City.id).all():
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))
    ses.close
