from utils.database import db
from sqlalchemy.sql import func


class Post(db.Model):
    __tablename__ = 'post'
    
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id'), nullable=False)
    createdate = db.Column(db.DateTime, default=func.now(), nullable=False)
    text = db.Column(db.Text())
    media = db.Column(db.String(255))
    topic = db.Column(db.String(100), nullable=False)
    
    user = db.relationship('User', back_populates = 'posts', passive_deletes = True)
    comments = db.relationship('Comment', back_populates='post', cascade ='all,delete')
    
    def __init__(self, title, user_id, text, media, topic):
        self.title = title
        self.user_id = user_id
        self.text = text
        self.media = media
        self.topic = topic
        
    