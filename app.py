from flask import Flask, render_template, request, redirect, url_for
from flask import flash
from flask_wtf.csrf import CSRFProtect
from flask import g

app = Flask(__name__)
csrf=CSRFProtect()

@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'),404

@app.route("/alumnos.html")
def alumnos():
	return render_template('alumnos.html')

@app.route("/")
@app.route("/index")
def index():
	return render_template("index.html")

if __name__ == '__main__':
	app.run(debug=True)
