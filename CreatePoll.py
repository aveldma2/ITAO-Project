from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from models.Base import *
from models.Question import Question
from models.Answer import Answer

start_poll = input('Would you like to create a poll? ')

# feedback: just use lower() function to escape case
while start_poll == 'Yes' or start_poll == "yes":
    num_questions = int(input('How many questions in your poll: '))

    for i in range(num_questions):
        # feedback: do the session stuff once, outside of the loop
        # then add and commit as much as you want
        
        session = sessionmaker()
        engine = create_engine('sqlite:///question.sqlite')
        session.configure(bind=engine)

        Base.metadata.create_all(engine)

        ses = session()

        q = Question()
        q.name = input('What is your question?  ')

        q.add_questionmark()

        ses.add(q)
        ses.commit()

        if q.name != '':

            answer_count = int(input('how many answers? '))

            for i in range(answer_count):
                n = input('answer options:  ')
                answer_options = Answer(option=n, question=q)
            q.validate()
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
