from models.Base import *

class Question(Base):
    __tablename__ = "questions"
    id = Column(Integer, primary_key=True)
    name = Column(String)

    def validate(self):
        if type(self.name) != str:
            print('not valid?')
            return False
        if len(self.answer_options) <= 1:
            raise 'Must have multiple answers'
            return False

    def add_questionmark(self):
        if self.name[-1] != '?':
            self.name = str(self.name + '?')
        return self.name

    def total_response_count(self):
        total = 0
        for i in self.answer_options:
            total = total + i.response_count()
        return total


