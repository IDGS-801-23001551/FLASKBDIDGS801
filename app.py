from flask import Flask, render_template, request, redirect, url_for
from flask import flash
from flask_wtf.csrf import CSRFProtect
from flask import g
from flask_migrate import  Migrate
from Maestros.routes import maestros
from Alumnos.routes import alumnos

from config import DevelopmentConfig
import forms
from models import db

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
app.register_blueprint(maestros)
app.register_blueprint(alumnos)
csrf=CSRFProtect()
db.init_app(app)
migrate=Migrate(app, db)

@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'),404


if __name__ == '__main__':
	csrf.init_app(app)
	
	with app.app_context():
		db.create_all()
	app.run(debug=True)

