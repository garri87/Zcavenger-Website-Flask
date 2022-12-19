from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager, current_user, login_user, logout_user, login_required



from config import config

from models.ModelUser import ModelUser

from models.entities.User import User

from datetime import datetime

import os

app = Flask(__name__)

csrf = CSRFProtect()

db = MySQL(app)

login_manager_app = LoginManager(app)

@login_manager_app.user_loader
def load_user(id):
    return ModelUser.get_by_id(db, id)

@app.route('/')
def index():
   
    return render_template('index.html')

@app.route('/development')
def development():
    
    return render_template('development.html')

@app.route('/login', methods=['GET','POST']) 
def login():
    
    if request.method == 'POST':
        
        user = User(0,request.form['username'], request.form['pass'])
        logged_user = ModelUser.login(db,user)
        if logged_user != None:
            if logged_user.contrasena:
                login_user = (logged_user)
                return redirect(url_for('index'))
            else: 
                flash('Invalid Password')
                return redirect(url_for('index'))

        else:
            flash('User Not Found')
            return redirect(url_for('index'))

    else:
        return redirect(url_for('index'))

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/register', methods = ['GET','POST'])
def register():
    
    if request.method == 'POST':
        _user = request.form['txtusername']
        _pass = request.form['txtpass']
        _pass2 = request.form['txtpass2']
        _realname = request.form['txtrealname']
        _mail = request.form['txtmail']
        _country = request.form['txtcountry']
        _profileimg = request.files['profileimg']
        
        if _pass == _pass2:
            print(_user)            
            if ModelUser.checkAvailability(db,_user) == True:
                
                flash('Registration Complete, Welcome!')               
                ModelUser.registerUser(db, _user, _pass, _mail,_realname, _country, _profileimg)
                
                return redirect(url_for('index'))
            else:
                flash('Username already exists')
        else: 
            flash("Passwords don't match")

    else:
        return render_template('register.html')


@app.route('/home')
def home(): 

    return render_template('home.html')


@app.route('/protected')
@login_required
def protected():
    return "<h1>Esta es una vista protegida, solo para usuarios autenticados.</h1>"

def status_401(error):
    return redirect(url_for('login'))

def status_404(error):
    return "<h1>Página no encontrada</h1>", 404
    
@app.route('/contactForm')
def contactForm():
    return render_template('contactForm.html')
   

if __name__ == '__main__':
    app.config.from_object(config['development'])
    csrf.init_app(app)
    app.register_error_handler(401, status_401)
    app.register_error_handler(404, status_404)
    app.run()
    
    
    

