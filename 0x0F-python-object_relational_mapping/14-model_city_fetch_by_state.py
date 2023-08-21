#!/usr/bin/python3
"""
Prints all City objects from the database hbtn_0e_14_usa.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City
from sys import argv


def main():
    """
    Main function that connects to the MySQL database and retrieves
    and displays all City objects sorted by their IDs.
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
    Session = sessionmaker(bind=engine)
    session = Session()
    cities = session.query(City).order_by(City.id).all()
    for city in cities:
        state = session.query(State).filter_by(id=city.State_id).first().name
        print("{}: ({}) {}".format(state, city.id, city.name))
    sessiton.close()


if __name__ == "__main__":
    main()
