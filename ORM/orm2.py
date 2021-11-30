from sqlalchemy import Column, ForeignKey, Integer, String, Text, Date, DateTime,create_engine
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Topic(Base):
    __tablename__ = "topic"
    __tableargs__ = {"comment": "Quotation themes"}


    topic_id = Column(Integer, nullable=False, unique=True, primary_key=True, autoincrement=True)
    topic_name = Column(String(255), comment = 'Topic name')
    description = Column(Text, comment = "Topic description")
    
    def __repr__ (self):
        return f'{self.topic_id}, {self.topic_name}, {self.description}'

class Author(Base):
    __tablename__ = "author"
    __tableargs__ = {"comment": "Authors of quotations"}

    author_id = Column(Integer, nullable=False, unique=True, primary_key=True, autoincrement=True)
    author_name = Column(String(255), comment="Author`s name")
    birth_date = Column(Date, comment= "Date of birth")
    country = Column(String(50), comment= "Where did the author come from")

    def __repr__ (self):
        return f"{self.author_id}, {self.name}, {self.birth_date}, {self.country}"

class Quote(Base):
    __tablename__ = "quote"
    __tableargs__ = {"comment": "Quotes"}

    quote_id = Column(Integer, nullable=False, unique=True, primary_key=True, autoincrement=True)
    text = Column(Text, comment="quote text")
    created_at = Column(DateTime, comment="Date and time of creation")
    author_id = Column(Integer, ForeignKey("author.author_id"), comment = "Quote author")
    topic_id = Column(Integer, ForeignKey('topic.topic_id'), comment="Theme of qoute")
    author = relationship("Author", backref="quote_author", lazy = "subquery")
    topic = relationship("Topic", backref="quote_topic", lazy = "subquery")

    def __repr__ (self):
        return f"{self.quote_id}, {self.created_at}, {self.author_id}, {self.topic_id}, {self.author}, {self.topic}"



if __name__ == "__main__":
    engine = create_engine("postgresql+psycopg2://postgres:password@10.0.17.42:5432/ormtest")
    Base.metadata.create_all(engine)


