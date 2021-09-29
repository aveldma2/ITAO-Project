from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from Base import *
from Question import Question
from Answer import Answer

start_poll = input('Would you like to create a poll? ')

while start_poll == 'Yes':
    num_questions = int(input('How many questions in your poll'))

    for i in range(num_questions):
        session = sessionmaker()
        engine = create_engine('sqlite:///question.sqlite')
        session.configure(bind=engine)

        Base.metadata.create_all(engine)

        ses = session()

        q = Question()
        q.name = input('What is your question?  ')

        ses.add(q)
        ses.commit()

        if q.name[-1] != '?':
            q.name = str(q.name + '?')

        if q.name != '':

            answer_count = int(input('how many answers? '))

            for i in range(answer_count):
                n = input('answer options:  ')
                answer_options = Answer(option=n, question=q)

            ses.add(q)
            ses.commit()

    questions = ses.query(Question).all()
    print(f'Congrats! You have created your poll with {num_questions} question(s)')
    print(f"Looping through {len(questions)} question(s)")
    for q in questions:
        print(str(q.id) + ' ' + q.name)
        for m in q.answer_options:
            print(f"-- {m.answer_options()}")
    break



