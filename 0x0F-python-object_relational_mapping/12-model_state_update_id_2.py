#!/usr/bin/python3
"""
Changes the name of a State object from the database hbtn_0e_6_usa.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv


def main():
    """
    Main function that connects to the MySQL database and changes the
    name of a State object in the database.
    """
    if len(argv) != 4:
        print("Usage: {} <username> <password> <db_name>"
              .format(argv[0]))
        return
    user = argv[1]
    password = argv[2]
    db_name = argv[3]
    new_name = "New Mexico"
    state_id = 2
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
             user, password, db_name), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    state = session.query(State).get(state_id)
    if state is not None:
        state.name = new_name
        session.commit()
    sessiton.close()


if __name__ == "__main__":
    main()
