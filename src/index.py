from app import app
from flask import redirect,url_for,flash
from decouple import config

from utils.database import db
from utils.mail import mail

from waitress import serve
from flask_wtf.csrf import CSRFProtect
import os

env = 'prod' # 'dev' or 'prod's

csrf = CSRFProtect()

app.config.from_pyfile('config.py')

db.init_app(app)
mail.init_app(app)


try:
  with app.app_context():
    db.create_all()  
    print("Connected to database!")
except:
    print("Error connecting to database")

    
def status_401(error):
    
    return redirect(url_for('auth.login'))

def status_404(error):
    return "<h1>404: Page not found </h1>", 404   
    
if __name__ == '__main__':
    app.config.from_pyfile('config.py')
    csrf.init_app(app)
    app.register_error_handler(401, status_401)
    app.register_error_handler(404, status_404)
    
    if env == 'dev':
        app.run(host="0.0.0.0", port= config('PORT'))
    else:
        serve(app, host="0.0.0.0",  port= config('PORT'), threads = 4) 


