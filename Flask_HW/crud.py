from flask import *
import sqlite3

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
#############################################################################
@app.route("/add")
def add():   
    return render_template("add.html")

@app.route("/savedetails",methods = ["POST","GET"])
def saveDetails():
    msg = ""
    if request.method == "POST":
        try:
            First_N = request.form["firstname"]
            Last_N = request.form["lastname"]
            Mobile_N = request.form["mnumber"]
            Office_N = request.form["onumber"]
            Mail = request.form["mail"]
            Addr = request.form["address"]
            with sqlite3.connect("contact.db") as connection:
                cursor = connection.cursor()   
                cursor.execute("""insert into addressbook (FirstName,LastName,MobileNumber,Officeroomnumber,Email,Address)
                values(?,?,?,?,?,?);""",(First_N,Last_N,Mobile_N,Office_N,Mail,Addr))
                connection.commit()
                msg = "Contact successfully added"   
        except:
            connection.rollback()
            msg = "Data is incorrect. Cannot add contact"
        finally:
            return render_template("success.html",message = msg)
            connection.close()
#############################################################################
@app.route("/update")
def update():
    return render_template("update.html")

@app.route("/updatedetails", methods = ["POST", "GET"])
def updateDetails():
    msg = ""
    if request.method == "POST":
        try:
            User_N = request.form["userid"]
            First_N = request.form["firstname"]
            Last_N = request.form["lastname"]
            Mobile_N = request.form["mnumber"]
            Office_N = request.form["onumber"]
            Mail = request.form["mail"]
            Addr = request.form["address"]
            with sqlite3.connect("contact.db") as connection:
                cursor = connection.cursor()
                cursor.execute("""update addressbook set FirstName=?,LastName=?,MobileNumber=?,Officeroomnumber=?,Email=?,Address=? where userid=?;""", (First_N,Last_N,Mobile_N,Office_N,Mail,Addr,User_N))
                connection.commit()
                msg = "Contact successfully changed"
        except:
            connection.rollback()
            msg = "Data is incorrect. Cannot change contact"
        finally:
            return render_template("success.html",message = msg)
            connection.close()  

#############################################################################
@app.route("/view")
def view():
	with sqlite3.connect("contact.db") as connection:
		connection.row_factory = sqlite3.Row
		cursor = connection.cursor() 
		cursor.execute("select * from addressbook")   
		data = cursor.fetchall()
		return render_template("view.html",rows = data)

@app.route("/delete")
def delete():
    return render_template("delete.html")

@app.route("/deleterecord",methods = ["POST"])   
def deleterecord():
    id = request.form["userid"]
    with sqlite3.connect("contact.db") as con:
        try:
            cur = con.cursor()
            cur.execute("delete from Addressbook where Userid= ?",id)
            msg = "Contact successfully Deleted"   
        except:
            msg = "Can't Be Deleted"
        finally:
            return render_template("delete_record.html",msg = msg)

if __name__ == "__main__":
    app.run(debug = True)  