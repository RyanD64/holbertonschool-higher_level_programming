#!/usr/bin/python3
"""deletes all State objects with a name containing the letter a from the db"""
from model_state import Base, State
from sys import argv
from sqlalchemy.orm import sessionmaker
from requests import Session
from sqlalchemy import create_engine


if __name__ == "__main__":
    eng = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                        .format(argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(eng)
    Session = sessionmaker(bind=eng)
    ses = Session()
    for state in ses.query(State).filter(State.name.like("%a%")):
        ses.delete(state)
    ses.commit()
    ses.close()
