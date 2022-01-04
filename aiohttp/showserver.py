from flask import *
import sqlite3

app = Flask(__name__)

@app.route("/")
def index():
	with sqlite3.connect("collected_data.db") as connection:
		connection.row_factory = sqlite3.Row
		cursor = connection.cursor() 
		cursor.execute("select * from parsedata")   
		data = cursor.fetchall()
		return render_template("view.html",rows = data)

if __name__ == "__main__":
    app.run(debug = True)  