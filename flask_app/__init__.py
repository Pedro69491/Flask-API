# file with the task to initialize the app
from flask_sqlalchemy import SQLAlchemy # layer between object oriented Python and the database
from flask import Flask
from flask_login import LoginManager # contains the code that lets my application and Flask-Login work together


db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__) # __name__(Python's module) where the app is located

    # config is the place where Flask stores configuration values, config is an atribute of the flask object
    app.config.from_object('config.Config') # Application Configuration

    # Initiating extensions
    db.init_app(app) # connect SQLAlchemy object with my application
    login_manager.init_app(app) # Configure app's object for login


    # blueprint for auth routes
    from .auth import api
    app.register_blueprint(api.auth_bp)

    return app



