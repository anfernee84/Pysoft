from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Date, Boolean, ForeignKey, String, Text, Table, create_engine, Integer
from sqlalchemy.orm import relationship, backref
from sqlalchemy.sql.expression import column, true

engine = create_engine("postgresql+psycopg2://postgres:password@10.0.17.42:5432/students")
Session = sessionmaker(bind=engine)
Base = declarative_base()


students_course_association = Table ("course_")


class Student(Base):
    __tablename__ = "student"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    surname = Column(String)
    birth_date = Column(Date)

    def __init__ (self, name, surname, birth_date):
        self.name = name
        self.surname = surname
        self.birth_date = birth_date

    def __repr__(self):
        return f"{self.name}, {self.surname}, {self.birth_date}"

    

class Course(Base):
    __tablename = "course"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(Text)

    def __init__ 

