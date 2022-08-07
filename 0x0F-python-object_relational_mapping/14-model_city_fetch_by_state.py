#!/usr/bin/python3
"""contains the class definition of a City"""
from model_state import State
from sys import argv
from sqlalchemy.orm import sessionmaker
from requests import Session
from sqlalchemy import create_engine
from model_city import City

if __name__ == "__main__":
    eng = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                        .format(argv[1], argv[2], argv[3], pool_pre_ping=True))
    Session = sessionmaker(bind=eng)
    ses = Session()
    for city, state in ses.query(City, State)\
                          .filter(City.state_id == State.id).order_by(City.id):
        print("{}: ({}) {}".format(state.name, city.id, city.name))
