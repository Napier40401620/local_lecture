from flask import Flask, render_template, jsonify, request, flash, url_for
import sqlite3, json

app = Flask(__name__)

@app.route('/')
def indexPage():
	return render_template('students.html')

@app.route('/save',methods=['GET','POST'])
def saveStudent():
	print("saving students" + request.method)
	error = ''
	if request.method == 'POST':
		print(request.form)
		name = request.form['Name']
		phy = int(request.form['Physics'])
		che = int(request.form['Chemistry'])
		math = int(request.form['Mathematics'])
		con = sqlite3.connect("../lectures/students.db")
		cur = con.cursor()
		cur.execute("insert into students(Name,Physics,Chemistry,Mathematics)values(?,?,?,?)",(name,phy,che,math))
		con.commit()
		print("execute")
		con.close()
		print("complete")
		return render_template("students.html",error=error)
	return render_template("students.html",error=error)

@app.route("/allstudents")
def studentInfo():
	con = sqlite3.connect("../lectures/students.db")
	cur = con.cursor()
	cur.execute("select * from students")
	rows = cur.fetchall()
	print(rows)
	return json.dumps(rows)

if __name__ == '__main__':
	app.run(debug=True)

