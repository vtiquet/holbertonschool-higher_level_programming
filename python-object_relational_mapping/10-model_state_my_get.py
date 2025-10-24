#!/usr/bin/python3
"""
Prints the State object with the name passed as argument
from the database hbtn_0e_6_usa.
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

if __name__ == "__main__":
    if len(sys.argv) != 5:
        pass

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name_search = sys.argv[4]

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            username, password, db_name
        ),
        pool_pre_ping=True
    )

    session = Session(engine)

    state = session.query(State).filter(
        State.name == state_name_search
    ).first()

    if state:
        print("{}".format(state.id))
    else:
        print("Not found")

    session.close()
