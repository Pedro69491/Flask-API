from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Email, DataRequired

class Registration(FlaskForm):
    username = StringField(
        'Username',
        validators=[DataRequired()]
    )
    email = StringField(
        'email',
        validators=[
            Email(message='Enter a vaild email.'),
            DataRequired()
            ]
    password = PasswordField(
        'Password',
        validators=[
            DataRequired(),
            length(min=6, message='Select a stronger password')
        ]
    )    
    )