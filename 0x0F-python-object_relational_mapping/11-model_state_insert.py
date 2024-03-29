#!/usr/bin/python3
""" This script adds the state object to the database """

if __name__ == '__main__':

    from sys import argv
    from sqlalchemy import create_engine
    from sqlalchemy.orm.session import sessionmaker, Session
    from model_state import Base, State

    username = '{}'.format(argv[1])
    password = '{}'.format(argv[2])
    db_name = '{}'.format(argv[3])

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, db_name))

    Session = sessionmaker(bind=engine)
    session = Session()

    session.add(State(name='Louisiana'))

    for state in session.query(State).filter(State.name == 'Louisiana'):
        print('{}'.format(state.id))

    session.commit()
