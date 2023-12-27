from flask import Blueprint,render_template,request,redirect,url_for
from flask_login import current_user

from models.entities.User import User

admin = Blueprint('admin',__name__)

@admin.route('/admin_dashboard')
def admin_dashboard():
    if current_user.privileges.is_admin: 
        users = User.query.all()
        
        return render_template('admin/admin_dashboard.html',users = users)
    else:
        
        return redirect(url_for('index'))
    
    