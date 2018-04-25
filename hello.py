from flask import Flask,render_template
app=Flask(__name__)

@app.route('/')
def defult(name=None):
	return ('Welcome to lcoalhost')

@app.route('/hello/<name>')
def hello(name=None):
	user={'name':name}
	return render_template('hello.html',user=user)

@app.route('/bootstrap')
def boot():
	return render_template('bootstrap.html'), 200



if __name__ == "__main__":
	app.run(debug=True)
