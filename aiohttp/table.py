import sqlite3
con=sqlite3.connect("collected_data.db")
cursor=con.cursor()
cursor.execute("""create table parsedata(Recid integer primary key autoincrement,
										URL varchar(100) not null,
										TimeResponse real not null,
										SiteResponse integer not null,
										ConType varchar(100) not null,
										SrvDate text not null,
										WebSrv text not null,
										Csettings text not null)""")
con.commit()
con.close()

print("Table Created Successfully")