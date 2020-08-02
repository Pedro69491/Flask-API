from flask_app import db
from .models import User
from flask import Blueprint, render_template, redirect, url_for, flash
from .forms import Registration, Login
from flask_login import ( 
    current_user,
    login_required,
    login_user, 
    logout_user
)


auth_bp = Blueprint('auth_bp', __name__, url_prefix='') # blueprint - name of class instance; __name__ - allows the system to know where blueprint is located, url_prefix eliminates url redundacies, since it's now prepended with all bp's URLs


#  The app decorator executes the main function every time the user enters this route on a specific domain 
@auth_bp.route('/')
def home():
    return 'hello world'

@auth_bp.route('/sign_up', methods=['GET', 'POST'])
def create_user():
    form = Registration()  # flask-wtf doesn't need to receive request.form, it loads automatically.
    if form.validate_on_submit(): # then validate_on_submit() checks if it is a POST request and if it is valid
        user = User.query.filter_by(username= form.username.data, email=form.email.data).first() # first user in the database with a specific email
        if user is None:
            new_user = User(
                username= form.username.data,
                email= form.email.data,
                password= form.password.data
            )
            new_user.set_password(form.password.data)
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user) # it's logged in but it's not authenticated
            return redirect(url_for('blueprint'))
        flash('User already exists')
    return render_template('register.html', form=form) # for instance of it isnt a POST request

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():

    # Bypass if the user is logged in
    if current_user.is_authenticated:
        return redirect(url_for('blueprint'))
    
    form = Login()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first() 
        if user and user.check_password(form.password.data): 
            login_user(user)
            return redirect(url_for())
        flash('Wrong user or password')
    return render_template('login.html', form=form)



    