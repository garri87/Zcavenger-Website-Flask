from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    SECRET_KEY = os.environ['SECRET_KEY']

class DevelopmentConfig(Config):
    DEBUG = True
    
    PROFILES_UPLOADS_FOLDER = os.path.join('uploads')
    
    MYSQL_HOST = os.environ['MYSQL_HOST']
    MYSQL_USER = os.environ['MYSQL_USER']
    MYSQL_PASSWORD = os.environ['MYSQL_PASSWORD']
    MYSQL_DB = os.environ['MYSQL_DB']
    
    MAIL_SERVER = os.environ['MAIL_SERVER']
    MAIL_PORT = os.environ['MAIL_PORT']
    MAIL_USERNAME = os.environ['MAIL_USERNAME']
    MAIL_PASSWORD = os.environ['MAIL_PASSWORD']
    MAIL_USE_TLS = os.environ['MAIL_USE_TLS']
    MAIL_USE_SSL = os.environ['MAIL_USE_SSL']    

class ProductionConfig(Config):
    DEBUG = False
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = ''
    MYSQL_DB = 'zcavengerdb'
    
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USERNAME = 'garri87games@gmail.com'
    MAIL_PASSWORD = 'tkhaftqwjpyotshj'
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True    
    
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}