from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.log import instance_logger
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Date, Boolean, ForeignKey, String, Text, Table, create_engine, Integer
from sqlalchemy.orm import relationship, backref


engine = create_engine("postgresql+psycopg2://postgres:password@10.0.17.42:5432/students")
Session = sessionmaker(bind=engine)
Base = declarative_base()


students_course_association = Table ("course_student", Base.metadata,
                            Column("course_id", Integer, ForeignKey("course.id")),
                            Column("students_id", Integer, ForeignKey("student.id")))


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
    __tablename__ = "course"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(Text)
    student = relationship("Student", secondary= students_course_association)

    def __init__(self, name, description):
        self.name = name
        self.description = description 

class Teacher(Base)
