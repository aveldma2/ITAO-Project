from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from models.Base import *
from models.Question import Question
from models.Answer import Answer
from models.UserAnswers import Response

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
    r = Response()
    r.answer_id = int(input('What is your answer? '))

    ses.add(r)
    ses.commit()

    res = r.answer_id

    responses = ses.query(Response).all()

    total = 0
    picked_count = 0
    for r in responses:
        total = total + 1
        if r.answer_id == res:
            picked_count = picked_count + 1

    percentage_picked = (picked_count/total)*100

    print(f'this answer is picked {percentage_picked}% of the time')

    another_question = input('Would you like to answer another question? ')
    if another_question == 'Yes':
        continue
    else:
        print('Thanks for taking the poll! ')
        break