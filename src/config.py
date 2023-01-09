from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    SECRET_KEY = os.environ['SECRET_KEY']

class DevelopmentConfig(Config):
    DEBUG = True
    ###
    UPLOADS_FOLDER = os.path.join('uploads')
    
    #MYSQL_URL = os. environ['MYSQL_URL']
    MYSQL_DB = os.environ['MYSQL_DB']
    MYSQL_HOST = os.environ['MYSQL_HOST']
    MYSQL_USER = os.environ['MYSQL_USER']
    MYSQL_PASSWORD = os.environ['MYSQL_PASSWORD']
    #MYSQL_PORT = os.environ['MYSQLPORT']
    
    MAIL_SERVER = os.environ['MAIL_SERVER']
    MAIL_PORT = os.environ['MAIL_PORT']
    MAIL_USERNAME = os.environ['MAIL_USERNAME']
    MAIL_PASSWORD = os.environ['MAIL_PASSWORD']
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True    

class ProductionConfig(Config):
    DEBUG = False
    
    UPLOADS_FOLDER = os.path.join('uploads')
    
    MYSQL_URL = os. environ['MYSQL_URL']
    MYSQL_DB = os.environ['MYSQLDATABASE']
    MYSQL_HOST = os.environ['MYSQLHOST']
    MYSQL_USER = os.environ['MYSQLUSER']
    MYSQL_PASSWORD = os.environ['MYSQLPASSWORD']
    MYSQL_PORT = os.environ['MYSQLPORT']
    
    MAIL_SERVER = os.environ['MAIL_SERVER']
    MAIL_PORT = os.environ['MAIL_PORT']
    MAIL_USERNAME = os.environ['MAIL_USERNAME']
    MAIL_PASSWORD = os.environ['MAIL_PASSWORD']
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True    
    
config = {
    'dev': DevelopmentConfig,
    'prod': ProductionConfig
}