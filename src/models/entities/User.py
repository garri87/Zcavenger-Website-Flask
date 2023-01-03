from werkzeug.security import check_password_hash
from flask_login import UserMixin

class User(UserMixin):
    
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
    
    