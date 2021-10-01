from models.Base import *
from models.Question import Question

class Answer(Base):
    __tablename__ = "answers"
    id = Column(Integer, primary_key=True)
    option = Column(String)

    question_id = Column(Integer, ForeignKey('questions.id'))
    question = relationship(Question, backref=backref('answer_options', uselist=True, cascade='delete,all'))

    def answer_options(self):
            return f"{self.id} {self.option}"

    #def answer_perc(self):
