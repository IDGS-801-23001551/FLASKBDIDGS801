from . import alumnos
import forms
from flask import Flask, render_template, request, redirect, url_for
from models import db, Alumnos, Curso


@alumnos.route("/alumnos.html", methods=['GET','POST'])
def crearAlumnos():
	create_form=forms.UserForm2(request.form)
	if request.method=='POST':
		alum=Alumnos(nombre=create_form.nombre.data,
			   apellidos=create_form.apellidos.data,
			   email=create_form.correo.data,
			   telefono=create_form.telefono.data)
		db.session.add(alum)
		db.session.commit()
		return redirect(url_for('alumnos.listadoAlumnos'))
	return render_template('alumnos/alumnos.html', form=create_form)

@alumnos.route("/listadoAlumnos")
def listadoAlumnos():
	create_from=forms.UserForm2(request.form)
	alumno=Alumnos.query.all()
	return render_template("alumnos/listadoAlumnos.html",form=create_from, alum=alumno)

@alumnos.route("/detalles",methods=['GET','POST'])
def detalles():
	if request.method=='GET':
		id=request.args.get('id')
		# Select * from alumnos where id==id
		alum1=db.session.query(Alumnos).filter(Alumnos.id==id).first()
		id=request.args.get('id')
		nombre=alum1.nombre
		apellidos=alum1.apellidos
		email=alum1.email
		telefono=alum1.telefono
		cursos=alum1.cursos
	return render_template("alumnos/detalles.html",id=id,nombre=nombre,apellidos=apellidos,email=email, telefono=telefono,cursos=cursos)

@alumnos.route("/modificar", methods=['GET','POST'])
def modificar():
	create_form=forms.UserForm2(request.form)
	if request.method=='GET':
		id=request.args.get('id')
		alum1=db.session.query(Alumnos).filter(Alumnos.id==id).first()
		create_form.id.data=request.args.get('id')
		create_form.nombre.data=str.rstrip(alum1.nombre)
		create_form.apellidos.data=alum1.apellidos
		create_form.correo.data=alum1.email
		create_form.telefono.data=alum1.telefono
	if request.method=='POST':
		id=create_form.id.data
		alum1=db.session.query(Alumnos).filter(Alumnos.id==id).first()
		alum1.id=id
		alum1.nombre=str.rstrip(create_form.nombre.data)
		alum1.apellidos=create_form.apellidos.data
		alum1.email=create_form.correo.data
		alum1.telefono=create_form.telefono.data
		db.session.add(alum1)
		db.session.commit()
		return redirect(url_for('alumnos.listadoAlumnos'))
	return render_template("alumnos/Modificar.html",form=create_form)

@alumnos.route('/eliminar', methods=['GET','POST'])
def eliminar():
	create_form=forms.UserForm2(request.form)
	if request.method=='GET':
		id = request.args.get('id')
		alum1 = db.session.query(Alumnos).filter(Alumnos.id == id).first()
		if alum1:
			create_form.id.data = alum1.id
			create_form.nombre.data = alum1.nombre
			create_form.apellidos.data = alum1.apellidos
			create_form.correo.data = alum1.email
			create_form.telefono.data = alum1.telefono
			return render_template("alumnos/eliminar.html", form=create_form)
	
	if request.method=='POST':
		id=create_form.id.data
		alum= db.session.query(Alumnos).filter(Alumnos.id == id).first()
		if alum:
			db.session.delete(alum)
			db.session.commit()
			return redirect(url_for('alumnos.listadoAlumnos'))
	return render_template("alumnos/eliminar.html", form=create_form)