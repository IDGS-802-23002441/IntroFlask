from wtforms import Form, RadioField, StringField, IntegerField
from wtforms import validators
from wtforms.validators import ValidationError


class cine_form(Form):

    nombre = StringField('Nombre', [
        validators.DataRequired(message="el campo es requerido"),
        validators.Length(min=3, max=100)
    ])

    personas = IntegerField('Personas', [
        validators.DataRequired(message="el campo es requerido"),
        validators.NumberRange(min=1, max=50)
    ])

    boletos = IntegerField('Boletos', [
        validators.DataRequired(message="el campo es requerido"),
        validators.NumberRange(min=1)  # 👈 SIN max fijo
    ])

    metodoPago = RadioField(
        'MetodoPago',
        choices=[('efectivo', 'Efectivo'), ('CINECO', 'CINECO')],
        validators=[validators.DataRequired(message="el campo es requerido")]
    )

    # 🔥 AQUÍ DEBE IR
    def validate_boletos(self, field):
        max_boletos = self.personas.data * 7

        if field.data > max_boletos:
            raise ValidationError(
                f"Máximo {max_boletos} boletos para {self.personas.data} persona(s)"
            )
