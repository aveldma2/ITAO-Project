from Base import *
from Question import Question
from Answer import Answer

class Response(Base):
    __tablename__ = 'responses'
    id = Column(Integer, primary_key=True)
    num_times = Column(Integer)
    count_res = Column(Integer)
    perc_res = Column(Integer)

    answer_id = Column(Integer, ForeignKey('answers.id'))
    answer = relationship(Answer, backref=backref('response_picks', uselist=True, cascade='delete,all'))

    def response_picks(self):
        return f"{self.id}"