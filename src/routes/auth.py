from flask import Blueprint, render_template, request, redirect, url_for, flash

from models.ModelUser import ModelUser

from models.entities.User import User

from flask_login import LoginManager, login_user, logout_user, login_required, current_user

from flask_mail import Mail, Message

from utils.db import db
from utils.mail import mail



auth = Blueprint('auth',__name__)


@auth.route('/login', methods=['GET','POST']) 
def login():
    
    if request.method == 'POST':
        
        user = User(0,request.form['username'], request.form['contrasena'])
        
        logged_user = ModelUser.login(db,user)
        if logged_user != None:
            if logged_user.contrasena and logged_user.is_active:
                login_user(logged_user)
                return redirect(url_for('home'))
            else: 
                flash('Invalid Credentials')
                print('logged user: '+ str(logged_user) )
                return redirect(url_for('index'))

        else:
            flash('Invalid Credentials')
            return redirect(url_for('index'))

    else:
        return redirect(url_for('index'))

@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/register', methods = ['GET','POST'])
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
                        
            if ModelUser.checkAvailability(db,_user) == True:
                
                msg = Message('Zcavenger.com | Please confirm your email address', sender = 'noreply@zcavenger.com', recipients= [_mail])
                msg.body = ""
                msg.html = render_template('auth/activationMail.html', _user = _user)
                mail.send(msg)
                
                flash('Registration Complete, a confirmation Mail was sent')               
                user = ModelUser.registerUser(db, _user, _pass, _mail,_realname, _country, _profileimg)
                
                current_user.is_active = False
                
                
                return redirect(url_for('index'))
            else:
                flash('Username already exists')
        else: 
            flash("Passwords don't match")

    else:
        return render_template('register.html')
