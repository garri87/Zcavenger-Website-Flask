from dotenv import load_dotenv
from decouple import config
import os

load_dotenv()

env = 'prod'

if env == 'dev':
    DEBUG = True
elif env == 'prod': 
    DEBUG = False 
    
SECRET_KEY = config('SECRET_KEY')

PORT = config('PORT')

user = config("MYSQL_USER")
password = config("MYSQL_PASSWORD")
host = config("MYSQL_HOST")
database = config("MYSQL_DB")
    
DATABASE_CONNECTION_URI = config('SQLALCHEMY_DATABASE_URI')

SQLALCHEMY_TRACK_MODIFICATIONS = False
  
UPLOADS_FOLDER = os.path.join('uploads')
      
MAIL_SERVER = config('MAIL_SERVER')
MAIL_PORT = config('MAIL_PORT')
MAIL_USERNAME = config('MAIL_USERNAME')
MAIL_PASSWORD = config('MAIL_PASSWORD')
MAIL_USE_TLS = False
MAIL_USE_SSL = True 

    
    
    


