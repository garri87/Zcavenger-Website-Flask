from flask import Flask, render_template, request, redirect, url_for, flash, send_from_directory

from config import config,DATABASE_CONNECTION_URI,SQLALCHEMY_TRACK_MODIFICATIONS

from flask_login import LoginManager, login_required

from flask_mail import Mail
  
from models.ModelUser import ModelUser

from routes.auth import auth
from routes.forum import forum

import utils.serializer as serializer 
from utils.database import db

import os


app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_CONNECTION_URI

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = SQLALCHEMY_TRACK_MODIFICATIONS

login_manager_app = LoginManager(app)

mail = Mail(app)

serializer.secretkey = app.config['SECRET_KEY']


@login_manager_app.user_loader
def load_user(id):
    
    return ModelUser.get_user(db,id) 

app.register_blueprint(auth)
app.register_blueprint(forum)

@app.route('/')
@app.route('/index') 
def index():
        
    return render_template('index.html')

@app.route('/development')
def development():
    
    return render_template('development.html')


@app.route('/home')
@login_required
def home(): 
    
    return render_template('home.html')
    
@app.route('/uploads/<fileName>')
def uploads(fileName):
    return send_from_directory(app.config['UPLOADS_FOLDER'], fileName)




