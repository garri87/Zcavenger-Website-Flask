from flask import Blueprint,render_template

from models.entities.User import User
from models.ModelUser import ModelUser

admin = Blueprint('admin',__name__)

@admin.route('/admin_dashboard')
def admin_dashboard():
    
    users = User.query.all()
    
    return render_template('admin_dashboard.html',users = users)
    
    