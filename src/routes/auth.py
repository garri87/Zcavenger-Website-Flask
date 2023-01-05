from flask import Blueprint, render_template, request, redirect, url_for, flash

from models.ModelUser import ModelUser

from models.entities.User import User

from flask_login import LoginManager, login_user, logout_user, login_required, current_user

from flask_mail import Mail, Message

from utils.db import db
from utils.mail import mail
from utils.serializer import s, SignatureExpired 
from itsdangerous import URLSafeTimedSerializer


auth = Blueprint('auth',__name__)


@auth.route('/login', methods=['GET','POST']) 
def login():
    
    if request.method == 'POST':
        
        user = User(0,request.form['username'], request.form['contrasena'])
        
        logged_user = ModelUser.login(db,user)
        if logged_user != None:
            if logged_user.contrasena:
                login_user(logged_user)
                if logged_user.active == True:
                    return redirect(request.referrer)
                else:
                    logout_user()
                    flash("User is not activated, please check your email")
                    return redirect(request.referrer)


            else: 
                flash('Invalid Credentials')
                print('logged user: '+ str(logged_user) )
                return redirect(request.referrer)

        else:
            flash('Invalid Credentials')
            return redirect(request.referrer)

    else:
        return redirect(request.referrer)

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
                        
            if ModelUser.checkAvailability(db,_user,_mail) == True:
                
                token  = s.dumps(_mail,salt='mail-confirm')

                sendActivationMail(_mail,_user,token)              
                ModelUser.registerUser(db, _user, _pass, _mail,_realname, _country, _profileimg,token,False)
                
                flash('Registration Complete, a confirmation Mail was sent to activate your account') 
                
                return redirect(url_for('index'))
            else:
                flash('Username already exists')
                return redirect(url_for('index'))
        else: 
            flash("Passwords don't match")
            return redirect(url_for('index'))

    else:
        return render_template('register.html')

@auth.route("/activate/<username>/<token>")
def activate(username = None, token = None):
    try:
        email = s.loads(token, salt='mail-confirm')
        
        user = ModelUser.get_User(db,None,username,email)
        print(email + " " + user.mail)
        if user.mail == email:
            ModelUser.activateUser(db,user.id,True)
            flash('User successfully activated')
            return redirect(url_for('index'))
        else:
            flash('Wrong activation token')
            return redirect(url_for('index'))
    except SignatureExpired:
    
        return
    
@auth.route('/deleteUser/<int:id>', methods=['GET', 'POST'])
@login_required
def deleteUser(id):
    if id == current_user.id:
        ModelUser.deleteUser(db,id)
        logout_user()
        flash('User deleted')
        return render_template('index.html')


    
def sendActivationMail(email,username,token):
                    
    msg = Message('Zcavenger.com | Activate your account', sender = 'noreply@zcavenger.com', recipients= [email])
                
    link = url_for('auth.activate', username = username, token = token, _external = True)
    msg.body = ""
    msg.html = render_template('auth/activationMail.html',username = username, email = email, token = token, link = link)
                
    mail.send(msg)
    
    return


