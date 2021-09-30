from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from Base import *
from Question import Question
from Answer import Answer
from UserAnswers import Response

session = sessionmaker()
engine = create_engine('sqlite:///question.sqlite')
session.configure(bind=engine)

Base.metadata.create_all(engine)

ses = session()

qs = ses.query(Question).all()

take_poll = input('Would you like to take a poll? ')

while take_poll == 'Yes':
    questions = ses.query(Question).all()

    for q in questions:
        print(str(q.id) + ' ' + q.name)
        for m in q.answer_options:
            print(f"-- {m.answer_options()}")
    num = int(input('Which question would you like to answer? '))
    q_to_answer = ses.query(Question).all()
    for q in q_to_answer:
        if q.id == num:
            print(q.name)
    res = int(input('What is your answer? '))

    response_picks = Response(id = res, answer=)

    another_question = input('Would you like to answer another question? ')
    if another_question == 'Yes':
        continue
    else:
        print('Thanks for taking the poll! ')
        break