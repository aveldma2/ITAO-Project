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

ans = ses.query(Answer).all()


for a in ans:
    print(a.question_id)
    print(a.option)
