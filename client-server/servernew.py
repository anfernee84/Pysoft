# import socket
# import threading
# import time

# def srv(host, port):
#     with socket.socket() as sock:
#         sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#         sock.bind((host,port))
#         sock.listen(2)
#         sock.setblocking(0)
#         conn, addr = sock.accept()
#         print(f"Connected by {addr}")
#         with conn:
#             while True:
#                 data = conn.recv(1024)
#                 print(f"From client: {data}")
#                 if not data:
#                     break
#                 conn.send(data.upper())


# def cli(host,port):
#     with socket.socket() as s:
#         while True:
#             try:
#                 s.connect((host,port))
#                 s.sendall(b"hello world")
#                 data = s.recv(1024)
#                 print(f"From server: {data}")
#                 break
#             except ConnectionRefusedError:
#                 time.sleep(0.5)

# HOST = "127.0.0.1"
# PORT = 34567

# server = threading.Thread(target=srv, args=(HOST,PORT))
# client = threading.Thread(target=cli, args =(HOST,PORT))

# server.start()
# client.start()
# server.join()
# client.join()
# print("Done")


# from http.server import HTTPServer, BaseHTTPRequestHandler
# from http import client
# import time
# import threading

# class SimpleReqHandler(BaseHTTPRequestHandler):

#     def do_GET(self):
#         self.send_response(200)
#         self.end_headers()
#         self.wfile.write(b"Hello, world")
    
#     def do_POST(self):
#         pass


# httpd = HTTPServer(("localhost", 8001), SimpleReqHandler)
# server = threading.Thread(target=httpd.serve_forever)
# server.start()
# time.sleep(0.5)

# h1 = client.HTTPConnection("localhost", 8001)
# h1.request("GET", "/")

# res = h1.getresponse()
# print(res.status, res.reason)
# data = res.read()
# print(data)
# httpd.shutdown()


# import dominate

# from dominate.tags import *

# doc = dominate.document(title='Dominate your HTML')

# with doc.head:
#     link(rel='stylesheet', href='style.css')
#     script(type='text/javascript', src='script.js')

# with doc:
#     with div(id='header').add(ol()):
#         for i in ['home', 'about', 'contact']:
#             li(a(i.title(), href='/%s.html' % i))

#     with div():
#         attr(cls='body')
#         p('Lorem ipsum..')

# print(doc)

# h = html()
# with h.add(body()).add(div(id='content')):
#     h1('Hello World!')
#     p('Lorem ipsum ...')
#     with table().add(tbody()):
#         l = tr()
#         l += td('One')
#         l.add(td('Two'))
#         with l:
#             td('Three')

# print(h)

# from jinja2 import Template

# name = 'Bill'
# age = 28

# tm = Template("My name is {{ name }} and I am {{ age }}")
# msg = tm.render(name=name, age=age)

# print(msg)  # My name is Bill and I am 28

# persons = [
#     {'name': 'Andrej', 'age': 34},
#     {'name': 'Mark', 'age': 17},
#     {'name': 'Thomas', 'age': 44},
#     {'name': 'Lucy', 'age': 14},
#     {'name': 'Robert', 'age': 23},
#     {'name': 'Dragomir', 'age': 54}
# ]

# rows_tmp = Template("""{% for person in persons -%}
#     {{ person.name }} {{ person.age }}
# {% endfor %}""")

# print(rows_tmp.render(persons=persons))

# from xml.etree import ElementTree
# from xml.etree.ElementTree import Element
# from xml.etree.ElementTree import SubElement

# membership = Element("membership")

# users = SubElement(membership, "users")

# SubElement(users, "user", name="john")
# SubElement(users, "user", name= "charles")
# SubElement(users, "user", name = "vasya")

# groups = SubElement(membership, "groups")

# group = SubElement(groups, "user", name = "users")

# SubElement(group, "user", name = "john")
# SubElement(group, "user", name = "charles")

# group = SubElement(groups, "group", name = "admin")

# SubElement(group, "user", name = "vasya")

# print (membership)

# import urllib.request

# with urllib.request.urlopen('http://www.python.org/') as req:
#     print (req.read(300))


import psycopg2
from psycopg2 import Error,DatabaseError, connect
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


# try:
#     connection = psycopg2.connect(
#         user = "postgres",
#         password = "password",
#         host = "10.0.17.42",
#         port = "5432",
#         database = "UserDB")
    
#     cursor = connection.cursor()

#     print ("Information about PostgreSQL")
#     print(connection.get_dsn_parameters(), "\n")

#     cursor.execute("SELECT version();")
#     record = cursor.fetchone()
#     print(f"You`re connected to {record}", "\n")

# except (Exception, Error) as error:
#     print ("Error", error)
# finally:
#     if connection:
#         cursor.close()
#         connection.close()
#         print("connection closed")


# def create_db():
#     try:
#         connection = psycopg2.connect(

#             user = "postgres",
#             password = "password",
#             host = "10.0.17.42",
#             port = "5432",)

#         connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
#         cursor = connection.cursor()
#         create_database = "CREATE DATABASE goit_db"
#         cursor.execute(create_database)
#         print ("DB has been created")
#     except (Exception, Error) as error:
#         print ("Error", error)
#     finally:
#         cursor.close()
#         connection.close()
#         print("connection closed")



# if __name__ == "__main__":
#     create_db()


# try:
#     connection = psycopg2.connect(
#         user = "postgres",
#         password = "password",
#         host = "10.0.17.42",
#         port = "5432",
#         database = "UserDB"
#         )
#     cursor = connection.cursor()
#     select_query = "select * from contacts where favorite = 'true'"
#     cursor.execute(select_query)
#     print ("Taking all records", "\n")
#     records = cursor.fetchall()

#     print ("Print each record", "\n")
#     for row in records:
#         print ("Phone", row[3], "\n")
#         print ("Email", row[2], "\n")
    
# except (Exception, Error) as error:
#         print ("Error", error)
# finally:
#         cursor.close()
#         connection.close()
#         print("connection closed")

# try:
#     connection = psycopg2.connect(
#         user = "postgres",
#         password = "password",
#         host = "10.0.17.42",
#         port = "5432",
#         database = "UserDB"
#         )
#     cursor = connection.cursor()
#     select_query = "select * from users"
#     cursor.execute(select_query)
#     user_query_first = cursor.fetchmany(3)
#     print ("Selecting two rows", "\n"*2)
#     for row in user_query_first:
#         print ("Email: ", row[2], "\n")
#         print ("Age: ", row[4], "\n")
#         print ("Date of creation: ", row[6], "\n"*2)

# except (Exception, Error) as error:
#         print ("Error", error)
# finally:
#         cursor.close()
#         connection.close()
#         print("connection closed")

def create_db():
    try:
        connection = psycopg2.connect(

            user = "postgres",
            password = "password",
            host = "10.0.17.42",
            port = "5432",)

        connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cursor = connection.cursor()
        create_database = "CREATE DATABASE phone_db"
        cursor.execute(create_database)
        print ("DB has been created")
    except (Exception, Error) as error:
        print ("Error", error)
    finally:
        cursor.close()
        connection.close()
        print("connection closed")


def insert_to_db():
    try:
        connection = psycopg2.connect(

            user = "postgres",
            password = "password",
            host = "10.0.17.42",
            port = "5432",
            database = "phone_db")
        cursor = connection.cursor()
        create_query = '''CREATE TABLE phone
                          (ID INT PRIMARY KEY     NOT NULL,
                          MODEL           TEXT    NOT NULL,
                          PRICE         INT   NOT NULL); '''

        cursor.execute(create_query)
        connection.commit()
        print("Successfully created table Phone at PostgreSQL")
        insert_query = """ INSERT INTO phone (ID, MODEL, PRICE)
                                           VALUES (%s,%s,%s)"""
        record_to_insert = (1, 'Iphone X', 950)
        cursor.execute(insert_query, record_to_insert)

        connection.commit()
        count = cursor.rowcount
        print(count, f"Record successfully added to table Phone")
    
    except (Exception, Error) as error:
        print ("Error", error)
    finally:
        cursor.close()
        connection.close()
        print("connection closed")    

def update_table(mobile_id, price):
    try:
        connection = psycopg2.connect(

            user = "postgres",
            password = "password",
            host = "10.0.17.42",
            port = "5432",
            database = "phone_db")
        cursor = connection.cursor()
        print("Table before update")
        select_query = """select * from phone where id = %s"""
        cursor.execute(select_query, (mobile_id,))
        record = cursor.fetchone()
        print(record)

        update_query = "UPDATE phone SET price = %s where id = %s"
        cursor.execute(update_query, (price, mobile_id,))
        connection.commit()
        count = cursor.rowcount
        print("Record has been updated", count)

        print("Table after update")
        cursor.execute(select_query, (mobile_id,))
        record = cursor.fetchone()
        print(record)

    except (Exception, Error) as error:
        print ("Error", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("connection closed")


def delete_data(mobile_id):
    try:
        connection = psycopg2.connect(

            user = "postgres",
            password = "password",
            host = "10.0.17.42",
            port = "5432",
            database = "phone_db")
        cursor = connection.cursor()
        delete_query = """DELETE FROM phone where ID = %s"""
        cursor.execute(delete_query, (mobile_id,))
        connection.commit()
        count = cursor.rowcount
        print(f"Record has been deleted {count}")

    except (Exception, Error) as error:
        print ("Error", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("connection closed")

def delete_table():
    with psycopg2.connect(user = "postgres", password = "password", host = "10.0.17.42", port = "5432", database = "phone_db") as connector:
        with connector.cursor() as cursor:
            cursor.execute ("DROP table phone")
    print("table has been deleted")

if __name__ == "__main__":
    create_db()
    insert_to_db()
    update_table(1,567)
    delete_data(1)
    delete_table()

