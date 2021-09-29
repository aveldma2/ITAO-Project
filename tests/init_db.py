# import what we need to get the db up and running
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from orm.models.base import *

# this method will be called at the beginning of tests to setup a db in memory
def init_db_session():
    session = sessionmaker()

    # setup db in memory, not a file
    engine = create_engine('sqlite:///:memory:')

    session.configure(bind=engine)

    # create all the tables
    Base.metadata.create_all(engine)

    # when you call this it will return the session to use to commit changes
    return session()

# you can use this to close it but not really necessary
def end_db_session(session):
    session.close()