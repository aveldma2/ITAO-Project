from models.Base import *
from models.Question import Question
from models.Answer import Answer

class Response(Base):
    __tablename__ = 'responses'
    id = Column(Integer, primary_key=True)

    answer_id = Column(Integer, ForeignKey('answers.id'))
    answer = relationship(Answer, backref=backref('response_picks', uselist=True, cascade='delete,all'))

    def response_picks(self):
        return f"{self.id}"

