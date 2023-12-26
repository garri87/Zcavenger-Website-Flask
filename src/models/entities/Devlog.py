from utils.database import db
from sqlalchemy.sql import func


class Devlog(db.Model):
    __tablename__ = 'devlog'
    
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    createdate = db.Column(db.DateTime, default=func.now(), nullable=False)
    text = db.Column(db.Text())
    media = db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)
                
    def __init__(self, title, text, media, user_id):
        self.title = title
        self.text = text
        self.media = media
        self.user_id = user_id