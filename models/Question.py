from models.Base import *

class Question(Base):
    __tablename__ = "questions"
    id = Column(Integer, primary_key=True)
    name = Column(String)

    def validate(self):
        if len(self.name) == 0:
            print('not valid?')
            return False

        if type(self.name) != String:
            print('not valid?')
            return False
