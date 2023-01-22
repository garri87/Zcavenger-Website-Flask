
from .entities.User import User
from werkzeug.security import generate_password_hash
from flask_login import login_user

from datetime import datetime

import os

class ModelUser():
    
    @classmethod
    def get_user(self, db, id = None ,usrname="", email = ""):
        """return a User() object by user id, username or email"""
        user = None
        try:
            if id != None:
                user = User.query.get(id)
            elif usrname != "":
                user = User.query.filter_by(username = usrname).first()
            elif email != "":
                user = User.query.filter_by(mail = email).first()    
          
            return User(user.id,user.username,user.password,user.realname,user.mail,user.country,user.createdate,user.profileimg,user.token,user.active) 
        except:
            return user
    
    
    @classmethod
    def login(self, db, user):
        """Login a User() and returns a complete User() object if credentials are correct"""
        try:
            #search for usename first
            query = User.query.filter_by(username = user.username).first()           
                                         
            if query != None:
                #if user is found check his password
                if User.check_password(query.contrasena,user.contrasena):
                    #if correct log in the user and return a user object
                    user = User(query.id,query.username,query.contrasena,query.realname,query.mail,query.country,query.createdate,query.profileimg,query.token,query.active)
                    login_user(user)
                    return user
                else:
                    return None
            else:
                return None
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    
    def register_user(self, db, usrname, password, email,name = "", country = "", profileimg = "", token = "", active = False):
        """Register a new user into db and returns a User() Object

        Args:
            db (SQLAlchemy()): Database to save
            usrname (string): Username
            password (string): Generates a password hash
            email (string): E-mail
            name (str, optional): Real Name. Defaults to "".
            country (str, optional): Country. Defaults to "".
            profileimg (str, optional): Profile Image. Defaults to "".
            token (str, optional): Activation Token. Defaults to "".
            active (bool, optional): User is active?. Defaults to False.

        Returns:
            User(): 
        """
    
        try:
            if User.query.filter_by(username = usrname).first() is None:
                           
                hashed_password = generate_password_hash(password)
                
                now = datetime.now()
                
                fileDate = now.strftime("%Y%H%M%S")
                
                if profileimg != "":
                    newprofileimg = fileDate + "_" + profileimg.filename
                    profileimg.save("src/uploads/" + newprofileimg)
                else:
                    newprofileimg = ""
                new_user = User(None,usrname,hashed_password,name,email,country,now,newprofileimg,token,active)
                db.session.add(new_user)
                db.session.commit()
                
                user = User.query.filter_by(username = new_user.username,mail = new_user.mail).first()
                            
                return User(user.id,user.username,user.contrasena,user.realname,user.mail,user.country,user.createdate,user.profileimg,user.token,user.active)
            else:
                
                return None
                
        
        
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod    
    def check_availability(self, usrname = "", email = ""):
        try:
            user = User.query.filter_by(username = usrname, mail = email).first()            
            
            if user != None:
                return False
            else:
                return True
            
        except Exception as ex:
            raise Exception(ex)
        
    

    @classmethod
    def activate_user(self,db,id,activate):
        try:
            user = User.query.get(id)
            user.active = activate
            db.session.commit()

        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def delete_user(self,db,id):   
        try:
            user = User.query.get(id)
            if user.profileimg != "":
                os.remove('src/uploads/' + user.profileimg)
            
            db.session.delete(user)          

            db.session.commit()
           
        except Exception as ex:
            raise Exception(ex)

    