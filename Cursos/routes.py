from . import cursos
import forms
from flask import Flask, render_template, request, redirect, url_for
from models import db, Curso, Maestros, Alumnos


@cursos.route('/ListadoCursos')
def listadoCursos():
    create_from=forms.UserForm4(request.form)
    curso=Curso.query.all()
    return render_template("cursos/listadoCursos.html",form=create_from, curso=curso)

@cursos.route('/AgregarCurso', methods=['GET','POST'])
def agregarCurso():
	create_form=forms.UserForm4(request.form)
	maestros = Maestros.query.all()
	create_form.maestro.choices=[(m.matricula,m.nombre)
							  for m in maestros]
	if request.method=='POST':
		curso=Curso(nombre=create_form.nombre.data,
			   descripcion=create_form.descripcion.data,
			   maestro_id=create_form.maestro.data)
		db.session.add(curso)
		db.session.commit()
		return redirect(url_for('cursos.listadoCursos'))
	return render_template("cursos/agregarCurso.html", form=create_form)

@cursos.route('/eliminarCurso', methods=['GET','POST'])
def eliminarCurso():
	create_form=forms.UserForm4(request.form)
	maestros = Maestros.query.all()
	create_form.maestro.choices=[(m.matricula,m.nombre)
							  for m in maestros]
	if request.method=='GET':
		id = request.args.get('id')
		curso = db.session.query(Curso).filter(Curso.id == id).first()
		if curso:
			create_form.id.data = curso.id
			create_form.nombre.data = curso.nombre
			create_form.descripcion.data = curso.descripcion
			create_form.maestro.data = curso.maestro
			return render_template("cursos/eliminarCurso.html", form=create_form)
			
	if request.method=='POST':
		id=create_form.id.data
		curso= db.session.query(Curso).filter(Curso.id == id).first()
		if curso:
			db.session.delete(curso)
			db.session.commit()
			return redirect(url_for('cursos.listadoCursos'))
	return render_template("cursos/eliminarCurso.html", form=create_form)

@cursos.route('/detallesCurso', methods=['GET','POST'])
def detalles():
	if request.method=='GET':
		id=request.args.get('id')
		# Select * from alumnos where id==id
		curso=db.session.query(Curso).filter(Curso.id==id).first()
		nombre=curso.nombre
		descripcion=curso.descripcion
		nombremaes=curso.maestro.nombre
		alumnos_curso = curso.alumnos
	return render_template("cursos/detallesCurso.html",id=id,nombre=nombre,descripcion=descripcion,maestro=nombremaes, alumnos_curso=alumnos_curso)


@cursos.route("/modificarCurso", methods=['GET','POST'])
def modificar():
	create_form=forms.UserForm4(request.form)
	maestros = Maestros.query.all()
	create_form.maestro.choices=[(m.matricula,m.nombre)
							  for m in maestros]
	if request.method=='GET':
		id=request.args.get('id')
		curso=db.session.query(Curso).filter(Curso.id==id).first()
		create_form.id.data=request.args.get('id')
		create_form.nombre.data=str.rstrip(curso.nombre)
		create_form.descripcion.data=curso.descripcion
		create_form.maestro.data=curso.maestro
	if request.method=='POST':
		id=create_form.id.data
		curso=db.session.query(Curso).filter(Curso.id==id).first()
		curso.id=id
		curso.nombre=str.rstrip(create_form.nombre.data)
		curso.descripcion=create_form.descripcion.data
		curso.maestro_id=create_form.maestro.data
		db.session.add(curso)
		db.session.commit()
		return redirect(url_for('cursos.listadoCursos'))
	return render_template("cursos/modificarCurso.html",form=create_form)

@cursos.route("/gestionarAlumnos")
def gestionarAlumnos():
	create_from=forms.UserForm2(request.form)
	id = request.args.get('id')
	curso = Curso.query.get(id)
	alumnos_curso = curso.alumnos
	alumnos_disponibles = Alumnos.query.filter(~Alumnos.cursos.any(Curso.id == id)).all()

	return render_template(
            "cursos/gestionarAlumnos.html",
			form=create_from,
            alumnos_curso=alumnos_curso,
            alumnos_disponibles=alumnos_disponibles,
            curso=curso
        )

@cursos.route("/agregarAlumno")
def agregarAlumno():
	id_alumno = request.args.get('alumno')
	id_curso = request.args.get('curso')

	alumno = Alumnos.query.get(id_alumno)
	curso = Curso.query.get(id_curso)

	if alumno and curso:
		curso.alumnos.append(alumno)
		db.session.commit()

	return redirect(url_for('cursos.gestionarAlumnos', id=id_curso))



@cursos.route("/eliminarAlumno")
def eliminarAlumno():
	id_alumno = request.args.get('alumno')
	id_curso = request.args.get('curso')

	alumno = Alumnos.query.get(id_alumno)
	curso = Curso.query.get(id_curso)

	if alumno and curso:
		curso.alumnos.remove(alumno)
		db.session.commit()

	return redirect(url_for('cursos.gestionarAlumnos', id=id_curso))