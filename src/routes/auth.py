from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import logout_user, login_required, current_user
from flask_mail import Message
from decouple import config

import requests

from models.ModelUser import ModelUser
from models.entities.User import User
from models.entities.Privileges import Privileges

from utils.database import db
from utils.mail import mail
from utils.serializer import s, SignatureExpired 
from utils.countries import countries


auth = Blueprint('auth',__name__)


@auth.route('/login', methods=['GET','POST']) 
def login():
    
    if request.method == 'POST':
        
        user = User(request.form['username'], request.form['contrasena'])
        
        try:
        
            logged_user = ModelUser.login(user)
        
        except:
            flash('An error ocurred, please try again later',category='login_message')

            logged_user = None
        
        if logged_user:
            
            if logged_user.active == True:
                
                return redirect(request.referrer)
            
            else:
                
                logout_user()
                
                flash("User is not activated, please check your email",category='login_message')
                
                return redirect(request.referrer)
        else: 
            
            flash('Invalid Credentials',category='login_message')
            return redirect(request.referrer)
    else:
        return redirect(request.referrer)    


@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

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
        
        secret_response = request.form['g-recaptcha-response']
        
        verify_response = requests.post(url=f"{config('RECAPTCHA_VERIFY_URL')}?secret={config('RECAPTCHA_SECRET_KEY')}&response={secret_response}").json()
            
        if verify_response["success"] == True:
            
            if _pass == _pass2:
                            
                if ModelUser.check_availability(_user,_mail) == True:
                    new_user = ModelUser.register_user(db, _user, _pass, _mail,_realname, _country, _profileimg,"",False)
                    
                    send_activation_mail(new_user)              
                
                    flash('Registration Complete, a confirmation Mail was sent to activate your account',category='general') 
                    
                    return redirect(url_for('index'))
                else:
                    flash('Username already exists', category='general')
                    return redirect(url_for('index'))
            else: 
                flash("Passwords don't match",category='general')
                return redirect(url_for('index'))
        else: 
            print('aborted')


    else:
        
        site_key = config('RECAPTCHA_SITE_KEY')
        
        return render_template('auth/register.html', site_key = site_key, countries = countries)

@auth.route("/activate/<username>/<token>")
def activate(username = None, token = None):
    try:
        email = s.loads(token, salt='mail-confirm')
        
        user = ModelUser.get_user(usrname=username,email=email)
        if user:
            if user.mail == email:
                ModelUser.activate_user(db,user.id,True)
                flash('User successfully activated',category='general')
                return redirect(url_for('index'))
            else:
                flash('Wrong activation token',category='general')
                return redirect(url_for('index'))
        else:
            flash('Error activating account: Not user found',category='general')

            return redirect(url_for('index'))
    except SignatureExpired:
    
        return
    
@auth.route('/deleteUser/<int:id>', methods=['GET', 'POST'])
@login_required
def deleteUser(id):
    if id == current_user.id:
        ModelUser.delete_user(db,id)
        logout_user()
        flash('Account was deleted',category='general')
        return redirect(url_for('index'))

@auth.route('/updateUser/<string:id>', methods=['GET', 'POST'])
def updateUser(id):
    user = User.query.get(id)
   
    if request.method == 'POST':
        _pass = request.form['txtpass']
        _pass2 = request.form['txtpass2']
        _mail = request.form['txtmail']
        _realname = request.form['txtrealname']
        _country = request.form['txtcountry']
        _profileimg = request.files['profileimg']
        
        if _pass == _pass2:
            user = ModelUser.update_user(db,id,_pass,_mail,_realname,_country,_profileimg)
            flash('Account successfully updated')
            return redirect(url_for('home'))
        else:
            flash('Passwords do not match')
    
    return render_template('auth/updateUser.html', user = user, countries = countries)

@auth.route('/user_dashboard/<int:user_id>')
@login_required
def user_dashboard(user_id): 
    user = ModelUser.get_user(id=user_id)
    return render_template('auth/user_dashboard.html', user = user)

    
    
def send_activation_mail(user):

    new_token  = s.dumps(user.mail,salt='mail-confirm')
                             
    msg = Message('Zcavenger.com | Activate your account', sender = 'noreply@zcavenger.com', recipients= [user.mail])
                
    link = url_for('auth.activate', username = user.username, token = new_token, _external = True)
    msg.body = ""
    msg.html = render_template('auth/activationMail.html',username = user.username, email = user.mail, token = new_token, link = link)
    
               
    mail.send(msg)
    query = User.query.get(user.id) 
    query.token = new_token
    db.session.commit()  
    
    return


