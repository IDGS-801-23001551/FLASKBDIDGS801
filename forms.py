from wtforms import Form, StringField
from wtforms import SearchField,IntegerField,PasswordField,FloatField, RadioField, TextAreaField, SelectField, HiddenField
from wtforms import EmailField
from wtforms import validators

class UserForm2(Form):
    id=IntegerField('id',
                    [validators.number_range(min=1, max=20, message='valor no valido')])
    nombre=StringField("Nombre",[
        validators.DataRequired(message="El nombre es requerido"),
        validators.length(min=4,max=20,message="Requiere min=4 max=20")
    ])
    apellidos=StringField("Apellidos",[
        validators.DataRequired(message="El apellido es requerido")
    ])
    correo=EmailField("Correo",[
        validators.DataRequired(message='el correo es requerido'),
        validators.Email(message="Ingresa correo valido")
    ])
    telefono=StringField('Telefono',
                          [validators.DataRequired(message="Ingresa un telefono valido")])
    
class UserForm3(Form):
    matricula=IntegerField('matricula',
                    [validators.number_range(min=1, max=20, message='valor no valido')])
    nombre=StringField("Nombre",[
        validators.DataRequired(message="El nombre es requerido"),
        validators.length(min=4,max=20,message="Requiere min=4 max=20")
    ])
    apellidos=StringField("Apellidos",[
        validators.DataRequired(message="El apellido es requerido")
    ])
    especialidad=StringField("Especialidad",[
        validators.DataRequired(message="La especialidad es requerida")
    ])
    correo=EmailField("Correo",[
        validators.DataRequired(message='el correo es requerido'),
        validators.Email(message="Ingresa correo valido")
    ])

class UserForm4(Form):
    id = HiddenField("id")
    nombre = StringField("Nombre", [
        validators.DataRequired(message="El nombre es requerido")
    ])
    descripcion = TextAreaField("Descripcion")
    maestro = SelectField(
        "Maestro",
        coerce=int,
        validators=[validators.DataRequired(message="Selecciona un maestro")]
    )