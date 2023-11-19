#!/usr/bin/python3
"""Adds the State object “Louisiana” to the database hbtn_0e_6_usa"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

if __name__ == "__main__":
    user = argv[1]
    passwd = argv[2]
    database = argv[3]

    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".
                           format(user, passwd, database), pool_pre_ping=True)

    session = Session(engine)

    new = State(name="Louisiana")
    session.add(new)
    session.commit()

    print(new.id)

    session.close()
