#!/usr/bin/python3
""" This script deletes all State objects with the name letter a """

if __name__ == '__main__':

    from sys import argv
    from sqlalchemy import create_engine
    from sqlalchemy.orm.session import sessionmaker, Session
    from model_state import Base, State

    username = '{}'.format(argv[1])
    passwd = '{}'.format(argv[2])
    db_name = '{}'.format(argv[3])

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(username, passwd, db_name))

    Session = sessionmaker(bind=engine)
    #Instantiate Session
    session = Session()

    session.query(State).filter(State.name.like('%a%')).delete(synchronize_session=False)

    session.commit()
