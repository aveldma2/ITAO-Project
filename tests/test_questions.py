import pytest

from models.Question import Question
from init_db import *
from models.Answer import Answer
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
        assert q.name == 'question?'

    #def test_question_mark(self):
     #   q = Question('question?')

      #  assert q.name == 'question?'


