#!/usr/bin/python3
"""
Adds the State object "Louisiana" to the database hbtn_0e_6_usa.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv


def main():
    """
    Main function that connects to the MySQL database and adds the
    State object "Louisiana" to the database.
    """
    if len(argv) != 4:
        print("Usage: {} <username> <password> <db_name>"
              .format(argv[0]))
        return
    user = argv[1]
    password = argv[2]
    db_name = argv[3]
    state_name = "Louisiana"
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
             user, password, db_name), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    new_state = State(name=state_name)
    session.add(new_state)
    session.commit()
    print(new_state.id)
    sessiton.close()


if __name__ == "__main__":
    main()
