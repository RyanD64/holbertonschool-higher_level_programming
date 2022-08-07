#!/usr/bin/python3
"""prints the first State object from the database hbtn_0e_6_usa"""
from model_state import Base, State
from sys import argv
from sqlalchemy.orm import sessionmaker
from requests import Session
from sqlalchemy import create_engine


if __name__ == "__main__":
    eng = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                        .format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(eng)
    Session = sessionmaker(bind=eng)
    ses = Session()
    first_state = ses.query(State).order_by(State.id).first()
    if first_state:
        print("{}: {}".format(first_state.id, first_state.name))
    else:
        print("Nothing")
    ses.close()
