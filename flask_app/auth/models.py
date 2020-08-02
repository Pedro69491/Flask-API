from flask_app import db, login_manager
from flask_login import UserMixin # This provides default implementations for the methods(ex: is_authenticated or is_active) that Flask-Login expects user objects to have
from werkzeug.security import generate_password_hash, check_password_hash
import datetime
import jwt # In order to create the the token



class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(80), unique=True)
    
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
        self.registered_on = datetime.datetime.now()

    def set_password(self, password):
        self.password = generate_password_hash(
            password,
            method= 'sha256'
        )
    
    def check_password(self, password):
        return check_password_hash(self.password, password) # self.password is hashed, the obj is a paremeter of set_password this way there ain't any scope problem
        
    def __repr__(self):
        return 'User: {}'.format(self.username) 


@login_manager.user_loader  
# Check if user is logged-in on every page load.
def load_user(id):
# user_loader callback function used to reload the user obj from the user_ID stored in the session, it returns the user obj  
    return User.query.filter_by(id=id).first()



@login_manager.unauthorized_handler
def unauthorized():
    """Redirect unauthorized users to Login page."""
    flash('You must be logged in to view that page.')
    return redirect(url_for('auth_bp.login'))
    


