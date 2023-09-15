from dotenv import load_dotenv
from decouple import config
import os

load_dotenv()

env = config('ENV')

if env == 'dev':
    DATABASE_CONNECTION_URI = 'mysql://root:@localhost/zcavengerdb'
    DEBUG = True
elif env == 'prod': 
    DATABASE_CONNECTION_URI = config('SQLALCHEMY_DATABASE_URI')
    DEBUG = False 
    
SECRET_KEY = config('SECRET_KEY')

MAX_CONTENT_LENGTH = 5120*5120
UPLOAD_EXTENSIONS = config('UPLOAD_EXTENSIONS')

PORT = config('PORT')

SQLALCHEMY_TRACK_MODIFICATIONS = False
  
UPLOADS_FOLDER = os.path.join('uploads')
      
MAIL_SERVER = config('MAIL_SERVER')
MAIL_PORT = config('MAIL_PORT')
MAIL_USERNAME = config('MAIL_USERNAME')
MAIL_PASSWORD = config('MAIL_PASSWORD')
MAIL_USE_TLS = False
MAIL_USE_SSL = True 

    
    
    


