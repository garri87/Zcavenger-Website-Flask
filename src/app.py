from flask import Flask, render_template, request, redirect, url_for, flash, send_from_directory
import requests

import settings

from flask_login import LoginManager

from flask_mail import Mail, Message
  
from models.ModelUser import ModelUser

from routes.auth import auth
from routes.forum import forum
from routes.admin import admin

import utils.serializer as serializer 
from flask_wtf.csrf import generate_csrf

app = Flask(__name__)

login_manager_app = LoginManager(app) 

mail = Mail(app)


serializer.secretkey = app.config['SECRET_KEY']


@login_manager_app.user_loader
def load_user(id):
    
    return ModelUser.get_user(id=id) 

app.register_blueprint(auth)
app.register_blueprint(forum)
app.register_blueprint(admin)

@app.context_processor
def csrf():
    csrf_token = generate_csrf()
    return {'csrf_token': csrf_token}
    
@app.route('/')
@app.route('/index') 
def index():
    site_key = settings.RECAPTCHA_SITE_KEY    
    return render_template('index.html', site_key = site_key)

@app.route('/development')
def development():
    
    return render_template('development.html')


@app.route('/contactForm', methods=['GET', 'POST'])
def contacForm():
    if request.method == 'POST':
        
        secret_response = request.form['g-recaptcha-response']
        
        verify_response = requests.post(url=f"{settings.RECAPTCHA_VERIFY_URL}?secret={settings.RECAPTCHA_SECRET_KEY}&response={secret_response}").json()
             
        if verify_response["success"] == True:
            _name = request.form['name']
            _email = request.form['email']
            _text = request.form['text']
            
            if all(char in _email for char in ['@', '.']):
                msg = Message('Zcavenger.com | New message', sender = 'noreply@zcavenger.com', recipients= ['garri87games@gmail.com'])

                msg.body = ""
                msg.html = render_template('contact/contactMessage.html', 
                                        name = _name, 
                                        email = _email, 
                                        text = _text)
                mail.send(msg)
                
                flash("Thank you, " + _name + " your message was received correctly", category='general')
                return redirect(url_for('index')) 
            else:
                flash("Please enter a valid E-mail",category='general')
                return redirect(url_for('index')) 

        else:
            print("Error")
            return redirect(url_for('index'))  

    
@app.route('/uploads/<fileName>')
def uploads(fileName):
    return send_from_directory(app.config['UPLOADS_FOLDER'], fileName)




