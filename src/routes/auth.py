from flask import Blueprint

from utils.db import db


auth = Blueprint('auth',__name__)


@auth.route('/login', methods=['GET','POST']) 
def login():
    
    if request.method == 'POST':
        
        user = User(0,request.form['username'], request.form['contrasena'])
        
        logged_user = ModelUser.login(db,user)
        if logged_user != None:
            if logged_user.contrasena:
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
    return redirect(url_for('login'))

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
                
                flash('Registration Complete, Please sign in with your credentials')               
                ModelUser.registerUser(db, _user, _pass, _mail,_realname, _country, _profileimg)
                
                return redirect(url_for('index'))
            else:
                flash('Username already exists')
        else: 
            flash("Passwords don't match")

    else:
        return render_template('register.html')
