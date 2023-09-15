from app import app
from flask import redirect,url_for,flash
from decouple import config
import settings

from utils.database import db
from utils.mail import mail
from utils.ckeditor import ckeditor

from waitress import serve
from flask_wtf.csrf import CSRFProtect
import os

config_file = 'settings.py'

app.config.from_pyfile(config_file)

csrf = CSRFProtect()

env = settings.env

db.init_app(app)
mail.init_app(app)
ckeditor.init_app(app)


try:
  with app.app_context():
    db.create_all()  
    print("Connected to database!")
    print("running on " + env)

except Exception as ex:
    print("Error connecting to database: -->" + str(ex))

    
def status_401(error):
    
    return redirect(url_for('auth.login'))

def status_404(error):
    return "<h1>404: Page not found </h1>", 404   
    
if __name__ == '__main__':
    app.config.from_pyfile(config_file)
    csrf.init_app(app)
    app.register_error_handler(401, status_401)
    app.register_error_handler(404, status_404)
    
    if env == 'dev':
        app.run()
    else:
        serve(app, host="0.0.0.0",  port= config('PORT'), threads = 4) 



