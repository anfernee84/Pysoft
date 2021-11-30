from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL
from psycopg2 import Error,DatabaseError, connect
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT, TRANSACTION_STATUS_ACTIVE
from sqlalchemy.orm import session, sessionmaker


DeclarativeBase = declarative_base()

class Post(DeclarativeBase):
    __tablename__ = "posts"

    id  = Column (Integer, primary_key=True)
    name = Column ("name", String)
    url = Column("url", String)

    def __repr__(self):
        return "".format(self.code)

def main():
    engine = create_engine("postgresql+psycopg2://postgres:password@10.0.17.42:5432/ormtest")
    DeclarativeBase.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    newpost = Post(name = "Two Record", url = "https://my.first.record")
    session.add(newpost)
    session.commit()


if __name__ == "__main__":
    main()


