from werkzeug.security import check_password_hash
from flask_login import UserMixin
from utils.database import db

class User(UserMixin,db.Model):

   id = db.Column(db.Integer(),primary_key=True)
   username = db.Column(db.String(40),nullable=False, unique=True)
   contrasena = db.Column(db.String(255),nullable=False)
   realname = db.Column(db.String(100))
   mail = db.Column(db.String(100),nullable=False, unique=True)
   country = db.Column(db.String(100))
   createdate = db.Column(db.DateTime)
   profileimg = db.Column(db.String(255))
   token = db.Column(db.String(255))
   active = db.Column(db.Boolean,default=False)           
   
   def __init__(self, id, username, contrasena = "", realname = "",mail = "",  country = "", createdate = "", profileimg = "", token = "", active = False) -> None:
      
       self.id = id
       self.username = username
       self.contrasena = contrasena
       self.realname = realname
       self.mail = mail
       self.country = country
       self.createdate = createdate
       self.profileimg = profileimg
       self.token = token
       self.active = active
        
    
   @classmethod
   def check_password(self, hashed_password, password):
       return check_password_hash(hashed_password, password)
    
    