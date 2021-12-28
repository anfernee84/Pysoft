import sqlite3
con=sqlite3.connect("contact.db")
cursor=con.cursor()
cursor.execute("""create table addressbook(Userid integer primary key autoincrement,
										   FirstName varchar(20) not null,
										   LastName varchar(20) null,
										   MobileNumber integer unique not null,
										   Officeroomnumber varchar(20) not null,
										   Email text not null unique,
										   Address text not null );""")
con.commit()
con.close()

print("Table Created Successfully")