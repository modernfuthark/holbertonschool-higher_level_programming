#!/usr/bin/python3
""" Using SQLAlchemy, get the first state from a database """


def Main():
    """ Main function """

    from sys import argv
    from model_state import Base, State
    # These must be import-protected
    # (don't remember if this was true or not, better safe than sorry)
    from sqlalchemy import create_engine
    from sqlalchemy.orm.session import Session, sessionmaker

    sql_username = str(argv[1])
    sql_passwd = str(argv[2])
    sql_dbname = str(argv[3])

    sqla_engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}"
        .format(sql_username, sql_passwd, sql_dbname)
        )

    Session = sessionmaker(bind=sqla_engine)
    sqla_session = Session()

    first_state = sqla_session.query(State).order_by(State.id).first()
    if first_state:
        print('{}: {}'.format(first_state.id, first_state.name))
    else:
        print("Nothing")

if __name__ == "__main__":
    Main()
