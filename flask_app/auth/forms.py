from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Email, DataRequired, Length

class Registration(FlaskForm):
    username = StringField(
        'Username',
        validators=[
            DataRequired()
            ]
    )
    email = StringField(
        'email',
        validators=[
            Email(message='Enter a valid email.'),
            DataRequired()
            ]
    )
    password = PasswordField(
        'Password',
        validators=[
            DataRequired(),
            Length(min=6, message='Select a stronger password')
        ]
    )  
    submit = SubmitField('Register')  

class Login(FlaskForm):
    username = StringField(
        'Username',
        validators=[
            DataRequired()
            ]
    )
    password = PasswordField(
        'Password',
        validators=[
            DataRequired()
        ]
    )
    submit = SubmitField('Log in')