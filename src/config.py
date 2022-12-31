import os

class Config:
    SECRET_KEY = 'bf555faaghwlhDS3fdseES'

class DevelopmentConfig(Config):
    DEBUG = True
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
    
    SECRET_KEY = 'b%"f555faaghwlhDS*3fdseES'
    
    
    
    
  
class ProductionConfig(Config):
    DEBUG = False
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = ''
    MYSQL_DB = 'zcavengerdb'
    
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}