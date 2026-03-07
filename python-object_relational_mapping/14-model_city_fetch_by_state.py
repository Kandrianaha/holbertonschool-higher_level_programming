#!/usr/bin/python3
"""Lists all city object with their State name"""
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost:3306/{database}",
        pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    results = session.query(State, City)\
        .filter(State.id == City.state_id)\
        .order_by(City.id)\
        .all()

    for state, city in results:
        print("{}: {} -> {}".format(city.id, city.name, state.name))

    session.close()
