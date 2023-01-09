from flask import Flask, render_template, redirect, url_for, send_from_directory

from flaskext.mysql import MySQL

from flask_wtf.csrf import CSRFProtect

from flask_login import LoginManager, login_required
from flask_mail import Mail
   
from config import config

from models.ModelUser import ModelUser

from routes.auth import auth
from routes.forum import forum

import utils.serializer as serializer 

import os

env = 'prod' #'dev'

app = Flask(__name__)

app.config.from_object(config[env])

csrf = CSRFProtect()

db = MySQL()

db.init_app(app)

login_manager_app = LoginManager(app)

mail = Mail(app)

serializer.secretkey = os.environ['SECRET_KEY']


@login_manager_app.user_loader
def load_user(id):
    
    return ModelUser.get_User(db,id) 

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
    conn = db.connect()
    cursor = conn.cursor()
    return render_template('home.html')
    
@app.route('/uploads/<fileName>')
def uploads(fileName):
    return send_from_directory(app.config['UPLOADS_FOLDER'], fileName)

def status_401(error):
    
    return redirect(url_for('auth.login'))

def status_404(error):
    return "<h1>404: Page not found </h1>", 404

if __name__ == '__main__':
    app.config.from_object(config[env])
    csrf.init_app(app)
    app.register_error_handler(401, status_401)
    app.register_error_handler(404, status_404)
    app.run()   
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080) 
