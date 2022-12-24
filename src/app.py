from flask import Flask, render_template, request, redirect, url_for, flash

from flask_mysqldb import MySQL

from flask_wtf.csrf import CSRFProtect

from flask_login import LoginManager, login_user, logout_user, login_required, current_user

from config import config

from models.ModelUser import ModelUser
from models.ModelPost import ModelPost

from models.entities.User import User
from models.entities.Post import Post

from routes.auth import auth
from routes.forum import forum


from datetime import datetime

import os


app = Flask(__name__)


csrf = CSRFProtect()

db = MySQL(app)

login_manager_app = LoginManager(app)

@login_manager_app.user_loader
def load_user(id):
    return ModelUser.get_by_id(db, id) 

app.register_blueprint(auth)
app.register_blueprint(forum)

@app.route('/') 
def index():
        
    return render_template('index.html')

@app.route('/development')
def development():
    
    return render_template('development.html')


@app.route('/home')
@login_required
def home(): 

    return render_template('home.html')
    
@app.route('/contactForm')
def contactForm():
    return render_template('contactForm.html')
   

def status_401(error):
    return redirect(url_for('login'))

def status_404(error):
    return "<h1>Página no encontrada</h1>", 404

if __name__ == '__main__':
    app.config.from_object(config['development'])
    csrf.init_app(app)
    app.register_error_handler(401, status_401)
    app.register_error_handler(404, status_404)
    app.run()
    
    

    
