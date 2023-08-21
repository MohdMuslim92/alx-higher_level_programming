#!/usr/bin/python3
"""
Creates the State 'California' with the City 'San Francisco' in the
database hbtn_0e_100_usa.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City
from sys import argv


def main():
    """
    Main function that connects to the MySQL database and creates
    the State 'California' with the City 'San Francisco'.
    """
    if len(argv) != 4:
        print("Usage: {} <username> <password> <db_name>"
              .format(argv[0]))
        return
    user = argv[1]
    password = argv[2]
    db_name = argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
             user, password, db_name), pool_pre_ping=True)
    Base.metadeta.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    state = State(name="California")
    city = City(name="San Francisco")
    state.cities.append(city)
    session.add(state)
    session.commit()
    session.close()


if __name__ == "__main__":
    main()
