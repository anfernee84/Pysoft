from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.log import instance_logger
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Date, Boolean, ForeignKey, String, Text, Table, create_engine, Integer
from sqlalchemy.orm import relationship, backref


engine = create_engine("postgresql+psycopg2://postgres:password@10.0.17.42:5432/assistant")
Session = sessionmaker(bind=engine)
Base = declarative_base()

class AddressBook(Base):
    __tablename__ = "addresssbook"

    