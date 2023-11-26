from utils.database import db
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func


class Comment(db.Model):
    __tablename__ = 'comment'
    
    id = db.Column(db.Integer(), primary_key=True)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    text = db.Column(db.Text())
    media = db.Column(db.String(255))
    createdate = db.Column(db.DateTime, default=func.now(), nullable=False)
    
    post = relationship('Post', back_populates='comments')
    user = relationship('User', back_populates='comments')

    def __init__(self, post_id, user_id, text, media):
        self.post_id = post_id
        self.user_id = user_id
        self.text = text
        self.media = media        
    