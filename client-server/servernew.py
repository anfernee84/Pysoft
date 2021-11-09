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
from psycopg2 import Error

try:
    connection = psycopg2.connect(
        user = "postgres",
        password = "password",
        host = "10.0.17.42",
        port = "5432",
        database = "UserDB")
    
    cursor = connection.cursor()

    print ("Information about PostgreSQL")
    print(connection.get_dsn_parameters(), "\n")

    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    print(f"You`re connected to {record}", "\n")

except (Exception, Error) as error:
    print ("Error", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print()

