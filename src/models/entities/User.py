from werkzeug.security import check_password_hash
from flask_login import UserMixin
from utils.database import db
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func


class User(UserMixin,db.Model):

   __tablename__ = 'user'
    
   id = db.Column(db.Integer(), primary_key=True)
   username = db.Column(db.String(40), nullable=False, unique=True)
   contrasena = db.Column(db.String(255), nullable=False)
   realname = db.Column(db.String(100))
   mail = db.Column(db.String(100), nullable=False, unique=True)
   country = db.Column(db.String(100))
   createdate = db.Column(db.DateTime, default=func.now())
   profileimg = db.Column(db.String(255))
   token = db.Column(db.String(255))
   active = db.Column(db.Boolean, default=False)
   
   privileges = relationship('Privileges', back_populates='user', uselist=False)
   posts = relationship('Post', back_populates='user')     
   comments = relationship('Comment', back_populates='user')    
   
   def __init__(self, username, contrasena="", realname="", mail="", country="", profileimg="", token="", active=False,privileges = None ):
        self.username = username
        self.contrasena = contrasena
        self.realname = realname
        self.mail = mail
        self.country = country
        self.profileimg = profileimg
        self.token = token
        self.active = active
        self.privileges = privileges
        
    
   @classmethod
   def check_password(self, hashed_password, password):
       return check_password_hash(hashed_password, password)
    
    