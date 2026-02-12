from wtforms import Form, StringField
from wtforms import SearchField,IntegerField,PasswordField,FloatField, RadioField
from wtforms import EmailField
from wtforms import validators

class UserForm2(Form):
    id=IntegerField('id',
                    [validators.number_range(min=1, max=20, message='valor no valido')])
    nombre=StringField("Nombre",[
        validators.DataRequired(message="El nombre es requerido"),
        validators.length(min=4,max=20,message="Requiere min=4 max=20")
    ])
    apaterno=StringField("Apaterno",[
        validators.DataRequired(message="El apellido es requerido")
    ])
    correo=EmailField("Correo",[
        validators.DataRequired(message='el correo es requerido'),
        validators.Email(message="Ingresa correo valido")
    ])
