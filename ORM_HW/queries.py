import datetime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.expression import delete, select, update
from mainmodule import AddressBook, Notes, Session
from sqlalchemy import insert, create_engine
from datetime import date


engine = create_engine("postgresql+psycopg2://postgres:password@10.0.17.42:5432/assistant")
Session = sessionmaker(bind=engine)
Base = declarative_base()


class DBAddressBook(AddressBook):

    def user_insert(lname,lphone,lemail,lbirthday, laddress):
        insrt = insert(AddressBook).values(name=lname,phone=lphone,email=lemail, birthday=lbirthday, address=laddress)
        conn = engine.connect()
        conn.execute(insrt)
        conn.close()

    def user_select(*args):
        slct = select(AddressBook).where(AddressBook.name == args)
        conn = engine.connect()
        result = conn.execute(slct)
        result_all = result.fetchall()
        for i in result_all:
            print(i)

    def user_update(lid,lname,lphone,lemail,lbirthday, laddress):
        upd = update(AddressBook).values(name=lname,phone=lphone,email=lemail, birthday=lbirthday, address=laddress).where(AddressBook.id == lid)
        conn = engine.connect()
        try:
            result = conn.execute(upd)
        except Exception as error:
            print (f"Text error: {error}")
        finally:
            conn.close()

    def delete_record(*args):
        dlt = delete(AddressBook).where(AddressBook.id == args)
        conn = engine.connect()
        conn.execute(dlt)
        conn.close()
    
    def all_user():
        slct = select(AddressBook)
        conn = engine.connect()
        result = conn.execute(slct)
        result_all = result.fetchall()
        for i in result_all:
            print(i)


class DBNotes(Notes):
    
    def note_insert(ltitle, lnote, ltag):
        insrt = insert(Notes).values(title = ltitle, note = lnote, tag = ltag)
        connect = engine.connect()
        connect.execute(insrt)
        connect.close()

    def note_select():
        note_select = select(Notes)
        connect = engine.connect()
        rslt = connect.execute(note_select)
        rslt_all = rslt.fetchall()
        for i in rslt_all:
            print (i)

    def note_delete(*args):
        dlt = delete(Notes).where(Notes.id == args)
        connect = engine.connect()
        connect.execute(dlt)
        connect.close()




# DBAddressBook.user_insert(lname="vasya2", lphone="0502921856", lemail="vasya@mail.ru", lbirthday=datetime.date(2019,6,29), laddress='some Street')
# DBAddressBook.user_select()
# DBAddressBook.delete_record(3)
# DBAddressBook.user_select("Jack")

# DBNotes.note_insert(ltitle="mYIR42ghwrethSTNOTE", lnote = "rthetyjnrrwtgh2hgwrtbh456h5hwe", ltag = "tag45r1, tag45gr4g22")
# DBNotes.note_select()
# DBNotes.note_delete(1)
# DBNotes.note_select()

