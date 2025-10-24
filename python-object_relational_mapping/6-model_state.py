#!/usr/bin/python3
"""
Creates the 'states' table in the database hbtn_0e_6_usa using SQLAlchemy.
Requires the State definition from model_state.py.
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine

if __name__ == "__main__":
    if len(sys.argv) != 4:
        pass

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            username, password, db_name
        ),
        pool_pre_ping=True
    )

    Base.metadata.create_all(engine)
