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

    r = input('What is your answer? ')

    res = Response()
    res.answer_id = r

    ses.add(res)
    ses.commit()

    answers = ses.query(Answer).all()
    for a in answers:
        print(f'{a.total_response_count()} people have taken the question and {a.answer_perc()}% answered this response')


    another_question = input('Would you like to answer another question? ')
    if another_question == 'Yes':
        continue
    else:
        print('Thanks for taking the poll! ')
        break

#how do we get the answer ids to change per question
#how do we query for just our specific answer id