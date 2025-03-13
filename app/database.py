from sqlalchemy import  create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import Column, Integer, Text
from .config import settings
from flask_login import UserMixin

engine = create_engine(settings.DATABASE_URL)
Base = declarative_base()
sessionLocal = sessionmaker(bind = engine)

def get_db():
    db= sessionLocal()
    return db

##attributes, method
class Student(Base, UserMixin):
    __tablename__ = 'students'
    studentid = Column(Integer, primary_key=True)
    firstname = Column(Text)
    lastname = Column(Text)
    password = Column(Text)
    email = Column(Text)
    admissionnumber = Column(Text)

def get_id(self):
    return str(self.studentid)
