from app import app
from flask import redirect, url_for
from decouple import config
import settings
from utils.database import db
from utils.mail import mail
from utils.ckeditor import ckeditor
from waitress import serve
from flask_wtf.csrf import CSRFProtect
import os

config_file = 'settings.py'

app.config.from_pyfile(config_file)

csrf = CSRFProtect(app)

csrf.secret_key = app.secret_key


db.init_app(app)
mail.init_app(app)
ckeditor.init_app(app)


try:
  with app.app_context():
    db.create_all()
    print("Connected to database!")
   

except Exception as ex:
    print("Error connecting to database: -->" + str(ex))

if not os.path.exists(settings.UPLOADS_FOLDER):
        os.makedirs(settings.UPLOADS_FOLDER)
        print('Uploads folder not found, creating one... ')

print("running on " + settings.env)
    
def status_401(error):
    
    return redirect(url_for('auth.login'))

def status_404(error):
    return "<h1>404: Page not found </h1>", 404   

app.register_error_handler(401, status_401)
app.register_error_handler(404, status_404)
    
if __name__ == '__main__':
    csrf.init_app(app)
        
    if settings.env == 'dev':
       app.run()
    else:
       serve(app, host=config('HOST'),  port= config('PORT'), threads = 4) 



