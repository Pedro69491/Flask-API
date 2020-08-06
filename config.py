from os import getenv # get environment variables
from dotenv import load_dotenv  # load configuration from .env 

load_dotenv() # it opens the .env

class Config:
    SECRET_KEY = getenv('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    POSTGRES = {
    'user': 'postgres',
    'pw': '135792468',
    'db': 'flaskExperiment',
    'host': 'localhost',
    'port': '5432'
    }
    SQLALCHEMY_DATABASE_URI = 'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES # Connect the app with the database using SQLALCHEMY


