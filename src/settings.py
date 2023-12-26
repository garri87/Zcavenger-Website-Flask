import os
from dotenv import load_dotenv
load_dotenv()

env = os.getenv('ENV')

if env == 'dev':
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
    DEBUG = True 
else:
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_POSTGRESQL_URI')
    DEBUG = False
    
SECRET_KEY = os.getenv('SECRET_KEY')
RECAPTCHA_SITE_KEY = os.getenv('RECAPTCHA_SITE_KEY')
RECAPTCHA_VERIFY_URL = os.getenv('RECAPTCHA_VERIFY_URL')
RECAPTCHA_SECRET_KEY = os.getenv('RECAPTCHA_SECRET_KEY')

MAX_CONTENT_LENGTH = 5120*5120
UPLOAD_EXTENSIONS = os.getenv('UPLOAD_EXTENSIONS')

PORT = os.getenv('PORT')

SQLALCHEMY_TRACK_MODIFICATIONS = False
  
UPLOADS_FOLDER = os.path.join(os.getcwd(),'uploads')
      
MAIL_SERVER = os.getenv('MAIL_SERVER')
MAIL_PORT = os.getenv('MAIL_PORT')
MAIL_USERNAME = os.getenv('MAIL_USERNAME')
MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
MAIL_USE_TLS = False
MAIL_USE_SSL = True 

    
    
    


