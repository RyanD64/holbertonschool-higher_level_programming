#!/usr/bin/python3
"""adds the State object “Louisiana” to the database hbtn_0e_6_usa"""
from model_state import State
from sys import argv
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


if __name__ == "__main__":
    eng = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                        .format(argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=eng)
    ses = Session()
    new_state = State(name="Louisiana")
    ses.add(new_state)
    ses.commit()
    print(new_state.id)
