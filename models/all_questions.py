from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from models.Base import *
from models.Question import Question
from Answer import Answer

session = sessionmaker()
engine = create_engine('sqlite:///question.sqlite')
session.configure(bind=engine)

Base.metadata.create_all(engine)

ses = session()

qs = ses.query(Question).all()

for q in qs:
    print(q.name)
