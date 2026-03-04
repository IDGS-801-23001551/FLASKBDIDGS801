from . import maestros
import forms
from flask import Flask, render_template, request, redirect, url_for
from models import db, Maestros



@maestros.route('/perfil/<nombre>')
def perfil(nombre):
    return f"Perfil de {nombre}"

@maestros.route('/ListadoMaestros')
def listadoMaestros():
    create_from=forms.UserForm2(request.form)
    maestros=Maestros.query.all()
    return render_template("maestros/listadoMaestros.html",form=create_from, maes=maestros)

@maestros.route('/AgregarMaestro', methods=['GET','POST'])
def agregarMaestro():
	create_form=forms.UserForm3(request.form)
	if request.method=='POST':
		maes=Maestros(nombre=create_form.nombre.data,
			   apellidos=create_form.apellidos.data,
               especialidad=create_form.especialidad.data,      
			   email=create_form.correo.data)
		db.session.add(maes)
		db.session.commit()
		return redirect(url_for('maestros.listadoMaestros'))
	return render_template("maestros/AgregarMaestro.html", form=create_form)

@maestros.route('/eliminarMaestro', methods=['GET','POST'])
def eliminarMaestro():
	create_form=forms.UserForm3(request.form)
	if request.method=='GET':
		matricula = request.args.get('matricula')
		maes = db.session.query(Maestros).filter(Maestros.matricula == matricula).first()
		if maes:
			create_form.matricula.data = maes.matricula
			create_form.nombre.data = maes.nombre
			create_form.apellidos.data = maes.apellidos
			create_form.especialidad.data = maes.especialidad
			create_form.correo.data = maes.email
			return render_template("maestros/eliminarMaestro.html", form=create_form)
			
	if request.method=='POST':
		matricula=create_form.matricula.data
		maes= db.session.query(Maestros).filter(Maestros.matricula == matricula).first()
		if maes:
			db.session.delete(maes)
			db.session.commit()
			return redirect(url_for('maestros.listadoMaestros'))
	return render_template("maestros/eliminarMaestro.html", form=create_form)

@maestros.route('/detallesMaestro', methods=['GET','POST'])
def detalles():
	if request.method=='GET':
		matricula=request.args.get('matricula')
		# Select * from alumnos where id==id
		maes=db.session.query(Maestros).filter(Maestros.matricula==matricula).first()
		matricula=request.args.get('matricula')
		nombre=maes.nombre
		apellidos=maes.apellidos
		especialidad=maes.especialidad
		email=maes.email
	return render_template("maestros/detallesMaestro.html",matricula=matricula,nombre=nombre,apellidos=apellidos,especialidad=especialidad,email=email)


@maestros.route("/modificarMaestro", methods=['GET','POST'])
def modificar():
	create_form=forms.UserForm3(request.form)
	if request.method=='GET':
		matricula=request.args.get('matricula')
		maes=db.session.query(Maestros).filter(Maestros.matricula==matricula).first()
		create_form.matricula.data=request.args.get('matricula')
		create_form.nombre.data=str.rstrip(maes.nombre)
		create_form.apellidos.data=maes.apellidos
		create_form.especialidad.data=maes.especialidad
		create_form.correo.data=maes.email
	if request.method=='POST':
		matricula=create_form.matricula.data
		maes=db.session.query(Maestros).filter(Maestros.matricula==matricula).first()
		maes.matricula=matricula
		maes.nombre=str.rstrip(create_form.nombre.data)
		maes.apellidos=create_form.apellidos.data
		maes.especialidad=create_form.especialidad.data
		maes.email=create_form.correo.data
		db.session.add(maes)
		db.session.commit()
		return redirect(url_for('maestros.listadoMaestros'))
	return render_template("maestros/modificarMaestro.html",form=create_form)
