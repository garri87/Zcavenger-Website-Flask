from flask import Flask, render_template, request, redirect, url_for, flash, send_from_directory
import git
import requests

from config import config,DATABASE_CONNECTION_URI,SQLALCHEMY_TRACK_MODIFICATIONS

from flask_login import LoginManager, login_required

from flask_mail import Mail, Message
  
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
    site_key = config('RECAPTCHA_SITE_KEY')    
    return render_template('index.html', site_key = site_key)

@app.route('/development')
def development():
    
    return render_template('development.html')


@app.route('/home')
@login_required
def home(): 
    
    return render_template('home.html')


@app.route('/contactForm', methods=['GET', 'POST'])
def contacForm():
    if request.method == 'POST':
        
        secret_response = request.form['g-recaptcha-response']
        
        verify_response = requests.post(url=f"{config('RECAPTCHA_VERIFY_URL')}?secret={config('RECAPTCHA_SECRET_KEY')}&response={secret_response}").json()
             
        if verify_response["success"] == True:
            _name = request.form['name']
            _email = request.form['email']
            _text = request.form['text']
            
            msg = Message('Zcavenger.com | New message', sender = 'noreply@zcavenger.com', recipients= ['garri87games@gmail.com'])

            msg.body = ""
            msg.html = render_template('contactMessage.html', 
                                       name = _name, 
                                       email = _email, 
                                       text = _text)
            mail.send(msg)
            
            flash("Thank you, " + _name + " your message was received correctly")
            return redirect(url_for('index')) 
        else:
            print("Error")
            return redirect(url_for('index'))  

    
@app.route('/uploads/<fileName>')
def uploads(fileName):
    return send_from_directory(app.config['UPLOADS_FOLDER'], fileName)




