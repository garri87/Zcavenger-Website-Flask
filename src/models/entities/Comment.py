from utils.database import db

class Comment(db.Model):
    
    id = db.Column(db.Integer(), primary_key=True)
    post_ID = db.Column(db.Integer())
    user_ID = db.Column(db.Integer())
    text = db.Column(db.String(100000))
    media = db.Column(db.String(255))
    createdate = db.Column(db.DateTime)    
    
    def __init__(self, id, post_ID, user_ID, text, media,createdate) -> None:
        self.id = id
        self.post_ID = post_ID
        self.user_ID = user_ID
        self.text = text
        self.media = media
        self.createdate = createdate
        
    