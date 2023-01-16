from utils.database import db


class Post(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(100))
    user_ID = db.Column(db.Integer())
    createdate = db.Column(db.DateTime)
    text = db.Column(db.String(1000))
    media = db.Column(db.String(255))
    topic = db.Column(db.String(100))
    
    def __init__(self, id, title, user_ID, createdate,text,media,topic) -> None:
        self.id = id
        self.title = title
        self.user_ID = user_ID
        self.createdate = createdate
        self.text = text
        self.media = media
        self.topic = topic
        
    