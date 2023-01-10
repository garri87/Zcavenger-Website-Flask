from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
"""
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
"""
class ProductionConfig(Config):
    DEBUG = False
    
    UPLOADS_FOLDER = os.path.join('uploads')
    
    MYSQL_URL = os.environ.get('MYSQL_URL')
    MYSQL_DB = os.environ.get('MYSQL_DB')
    MYSQL_HOST = os.environ.get('MYSQL_HOST')
    MYSQL_USER = os.environ.get('MYSQL_USER')
    MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD')
    MYSQL_PORT = os.environ.get('MYSQL_PORT')
    
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = os.environ.get('MAIL_PORT')
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True    
    
config = {
   # 'dev': DevelopmentConfig,
    'prod': ProductionConfig
}