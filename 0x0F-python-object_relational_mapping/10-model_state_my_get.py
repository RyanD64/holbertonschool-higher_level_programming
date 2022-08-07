#!/usr/bin/python3
"""prints the State object with the name passed as argument from the db"""
from unicodedata import name
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
    state = ses.query(State).filter_by(name=argv[4]).first()
    if state:
        print("{}".format(state.id))
    else:
        print("Not found")
    ses.close()
