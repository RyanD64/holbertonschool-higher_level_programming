#!/usr/bin/python3
""" creates the State “California” with the City “San Francisco” from the db"""
from requests import session
from relationship_state import Base, State
from relationship_city import City
from sys import argv
from sqlalchemy.orm import Session
from sqlalchemy import create_engine


if __name__ == "__main__":
    eng = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                        .format(argv[1], argv[2], argv[3], pool_pre_ping=True))

    Base.metadata.create_all(eng)

    ses = Session(eng)
    new_city = City(name="San Francisco")
    new_state = State(name="California")
    new_state.cities.append(new_city)
    ses.add_all([new_state, new_city])

    ses.commit()
    ses.close
