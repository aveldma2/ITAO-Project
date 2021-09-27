from sqlalchemy import Column, DateTime, String, Integer, ForeignKey, func
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from Question import Question
from Base import *


class Answer(Base):
    __tablename__ = "answers"
    id = Column(Integer, primary_key=True)
    answer_type = Column(String)

    question_id = Column(Integer, ForeignKey('questions.id'))
    question = relationship(Question, backref=backref('answers', uselist=True, cascade='delete,all'))