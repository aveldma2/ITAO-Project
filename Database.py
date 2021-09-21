from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Question(Base):
    __tablename__ = 'question'
    id = Column(Integer, primary_key=True)
    question = Column(String)
    answer = relationship('Answer', secondary='question_answer_link')

class Answer(Base):
    __tablename__ = 'answer'
    id = Column(Integer, primary_key=True)
    answer = Column(String)
    question_id = Column(Integer, ForeignKey('question.id'))
    question = relationship('Question', secondary='question_answer_link')


class QuestionAnswerLink(Base):
    __tablename__ = 'question_answer_link'
    question_id = Column(Integer, ForeignKey('question.id'), primary_key=True)
    answer_id = Column(Integer, ForeignKey('answer.id'), primary_key=True)


from sqlalchemy import create_engine
engine = create_engine('sqlite:///')

from sqlalchemy.orm import sessionmaker
session = sessionmaker()
session.configure(bind=engine)
Base.metadata.create_all(engine)
