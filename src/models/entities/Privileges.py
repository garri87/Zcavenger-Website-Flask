
from utils.database import db


class Privileges(db.Model):

   __tablename__= 'privileges'
    
   id = db.Column(db.Integer(), primary_key=True)
   user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
   is_admin = db.Column(db.Boolean,default=False)
   can_comment = db.Column(db.Boolean,default=False)
   can_post = db.Column(db.Boolean,default=False)
   rank = db.Column(db.String(30),nullable=True)
   
   user = db.relationship('User', back_populates = 'privileges')
   
   def __init__(self,is_admin,can_comment,can_post,rank):
      self.is_admin = is_admin
      self.can_comment = can_comment
      self.can_post = can_post
      self.rank = rank