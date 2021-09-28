from Base import *
from Question import Question

class Answer(Base):
    __tablename__ = "answers"
    id = Column(Integer, primary_key=True)
    option = Column(String)

    question_id = Column(Integer, ForeignKey('questions.id'))
    question = relationship(Question, backref=backref('answer_options', uselist=True, cascade='delete,all'))

