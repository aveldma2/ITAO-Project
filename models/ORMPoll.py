from sqlalchemy.orm import sessionmaker
session = sessionmaker()

from sqlalchemy import create_engine

engine = create_engine('sqlite:///question.sqlite')
session.configure(bind=engine)

from Question import Question
from Answer import Answer

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

Base.metadata.create_all(engine)

ses = session()

q = Question()
q.name = input('What is your question')

#if q.name != '':

 #   answer_count = int(input('how many answers '))

  #  for i in range(answer_count):
   #     n = input('answer options:')
    #    member = Answer(answer=n, question = q)

ses.add(q)
ses.commit()

questions = ses.query(Question).all()
#for q in questions:
  #  print(q)
 #   for m in q.answers:
     # print(m)