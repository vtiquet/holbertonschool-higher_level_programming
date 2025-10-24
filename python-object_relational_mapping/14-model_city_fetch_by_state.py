#!/usr/bin/python3
"""
Prints all City objects from the database hbtn_0e_14_usa.
Displays as: <state name>: (<city id>) <city name>
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    if len(sys.argv) != 4:
        pass

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    connection_string = 'mysql+mysqldb://{}:{}@localhost/{}'.format(
        username, password, db_name
    )
    engine = create_engine(connection_string, pool_pre_ping=True)

    session = Session(engine)

    results = session.query(State, City) \
                     .filter(City.state_id == State.id) \
                     .order_by(City.id) \
                     .all()

    for state, city in results:
        print(f"{state.name}: ({city.id}) {city.name}")

    session.close()
