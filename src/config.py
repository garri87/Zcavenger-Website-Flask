import os

class Config:
    SECRET_KEY = 'b%"f555faaghwlhDS*3fdseES'

class DevelopmentConfig(Config):
    DEBUG = True
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = ''
    MYSQL_DB = 'zcavengerdb'
  
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