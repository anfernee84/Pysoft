from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.log import instance_logger
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Date, Boolean, ForeignKey, String, Text, Table, create_engine, Integer
from sqlalchemy.orm import relationship, backref


engine = create_engine("postgresql+psycopg2://postgres:password@10.0.17.42:5432/assistant")
Session = sessionmaker(bind=engine)
Base = declarative_base()

class AddressBook(Base):
    __tablename__ = "addressbook"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    phone = Column(String)
    email = Column(String)
    birthday = Column(Date)
    address = Column(String)

    def __init__ (self, name, phone, email, birthday, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.birthday = birthday
        self.address = address

    def __repr__(self):
        return f"{self.name}, {self.phone}, {self.email}, {self.birthday}, {self.address}"


class Notes(Base):

    __tablename__ = "note"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    note = Column(String)
    tag = Column(String)

    def __init__ (self, title, note, tag):
        self.title = title
        self.note = note
        self.tag = tag

    def __repr__(self):
        return f'{self.title}, {self.note}, {self.tag}'

