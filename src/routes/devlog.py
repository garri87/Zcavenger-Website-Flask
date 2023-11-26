from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import logout_user, login_required, current_user
from models.entities.Devlog import Devlog
from models.ModelDevlog import ModelDevlog

from utils.database import db
from utils.mail import mail
from utils.serializer import s, SignatureExpired 
from utils.countries import countries

auth = Blueprint('auth',__name__)

@auth.route('/create_devlog', methods=['GET','POST']) 
@login_required
def create_devlog():

    if request.method == 'POST':
        title = request.form.get()
        text = request.form.get('ckeditor')
        media = request.files['media']

        ModelDevlog.create_devlog(db,title,text,media)
            
    else:
        pass
    
    
    return redirect(url_for('devlog'))