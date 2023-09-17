#!/usr/bin/python3
""" It prints all City objects from the database hbtn_0e_14_usa """

if __name__ == '__main__':

    from sys import argv
    from sqlalchemy import create_engine
    from sqlalchemy.orm.session import Session, sessionmaker
    from model_state import Base, State
    from model_city import City

    username = '{}'.format(argv[1])
    passwd = '{}'.format(argv[2])
    db_name = '{}'.format(argv[3])

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, passwd, db_name))

    Session = sessionmaker(bind=engine)
    # Instantiate session
    session = Session()

    for state, city in session.query(State, City).\
            filter(State.id == City.state_id).order_by(City.id):
        print('{}: ({}) {}'.format(state.name, city.id, city.name))
