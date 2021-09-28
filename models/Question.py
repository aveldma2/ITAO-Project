from sqlalchemy import Column, DateTime, String, Integer, ForeignKey, func
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from Base import *

class Question(Base):
    __tablename__ = "questions"
    id = Column(Integer, primary_key=True)
    name = Column(String)

