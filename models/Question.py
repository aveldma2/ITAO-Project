from models.Base import *

class Question(Base):
    __tablename__ = "questions"
    id = Column(Integer, primary_key=True)
    name = Column(String)

    def validate(self):
        if type(self.name) != str:
            print('not valid?')
            return False

    def add_questionmark(self):
        if self.name[-1] != '?':
            self.name = str(self.name + '?')

        return self.name

