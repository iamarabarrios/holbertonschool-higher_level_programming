#!/usr/bin/python3
"""
Write a Python file similar to model_state.py
named model_city.py that contains
the class definition of a City.
"""

from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


if __name__ == "__main__":
    user = argv[1]
    passwd = argv[2]
    database = argv[3]

    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".
                           format(user, passwd, database), pool_pre_ping=True)

    session = Session(engine)

    sql = session.query(State, City).\
        filter(City.state_id == State.id).\
        order_by(City.id).all()

    for state, city in sql:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()
