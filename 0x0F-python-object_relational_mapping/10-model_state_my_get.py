#!/usr/bin/python3
"""
Prints the State object with the given name from the database hbtn_0e_6_usa.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv


def main():
    """
    Main function that connects to the MySQL database and retrieves the
    State object with the specified name.
    """
    if len(argv) != 5:
        print("Usage: {} <username> <password> <db_name> <state_name>"
              .format(argv[0]))
        return
    user = argv[1]
    password = argv[2]
    db_name = argv[3]
    state_name = argv[4]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
             user, password, db_name), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    state = session.query(State).filter(
                            State.name == state_name).first()
    if state is not None:
        print(state.id)
    else:
        print("Not found")

    sessiton.close()


if __name__ == "__main__":
    main()
