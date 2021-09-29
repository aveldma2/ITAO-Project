import pytest
from models.Question import Question
from init_db import *
from models.Answer import Answer

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
        q = Question('1234')
        assert p.validate() == False