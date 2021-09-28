from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from Base import *
from Question import Question
from Answer import Answer

session = sessionmaker()
engine = create_engine('sqlite:///question.sqlite')
session.configure(bind=engine)

Base.metadata.create_all(engine)

ses = session()

qs = ses.query(Question).all()

for q in qs:
    print(q.name)
    for ans in q.answers:
        print(ans.option)
        aq