#!/usr/bin/python3
"""All states via SQLAlchemy."""

import sys
from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    """Main function."""

    conn = 'mysql+mysqldb://{}:{}@localhost/{}'
    engine = create_engine(conn.format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()

    states = (session.query(State, func.row_number()
                            .over(order_by=State.id)
                            .label('row_number'))
                            .all())

    for row in states:
        print(f"{row.row_number}: {row.State.name}")
