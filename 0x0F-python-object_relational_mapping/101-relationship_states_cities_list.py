#!/usr/bin/python3
"""lists all State objects, and City objects, contained in the db"""
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
    for state in ses.query(State).order_by(State.id).all():
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("    {}: {}".format(city.id, city.name))
    ses.close
