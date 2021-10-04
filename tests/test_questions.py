import pytest

from models.Question import Question
from init_db import *
from models.Answer import Answer
from models.UserAnswers import Response
from models.Base import *

class TestQuestion:

    def test_db(self):
        ses = init_db_session()

        assert ses.query(Question).count() == 0

        question = Question()
        a = Answer(option='Yes', question=question)
        ses.add(a)
        ses.commit()

        assert ses.query(Answer).count() == 1
        assert ses.query(Question).count() == 1

    def test_name_nonnumeric(self):
        lis = ['1234', '']

        for q in lis:
            q = Question()

        assert q.validate() == False

    def test_question_mark(self):
        q = Question()
        q.name = 'question'
        q.add_questionmark()
        assert q.name == 'question?'

    def test_question_mark_runs(self):
        q = Question()

        q.name = 'question?'
        q.add_questionmark()

        assert q.name == 'question?'

class TestResponse:

    def test_resdb(self):
        ses = init_db_session()

        assert ses.query(Question).count() == 0

        question = Question()
        a = Answer(option='Yes', question=question)
        r = Response(answer=a)
        ses.add(r)
        ses.commit()

        assert ses.query(Response).count() == 1

    def test_percentage(self):
        ses = init_db_session()


        q = Question()
        q.name = 'Question'

        answer1 = Answer(option='x', question=q)
        answer2 = Answer(option='y', question=q)

        #ses.add(q)
       # ses.commit()

        response1 = Response(answer=answer1)
        response2 = Response(answer=answer1)
        response3 = Response(answer=answer2)

        assert q.total_response_count() == 3
        assert answer1.response_count() == 2
        assert answer1.total_response_count() == q.total_response_count()
        assert answer1.answer_perc() == 66



