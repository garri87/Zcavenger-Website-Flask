
from flask import flash, redirect, request
from .entities.User import User
from .entities.Privileges import Privileges
from werkzeug.security import generate_password_hash
from flask_login import login_user
from datetime import datetime
import settings
import os
from utils.uploads import upload_image

class ModelUser():
    
    @classmethod
    def get_user(self, id = None ,usrname="", email = ""):
        """return a User() object by user id, username or email"""
        user = None
        try:
            if id != None:
                user = User.query.get(id)
            elif usrname != "":
                user = User.query.filter_by(username = usrname).first()
            elif email != "":
                user = User.query.filter_by(mail = email).first()    
          
            return user 
        except:
            return user
    
    
    @classmethod
    def login(self, user):
        """Login a User() and returns User() object if credentials are correct"""
        try:
            #search for usename first
            query = User.query.filter(User.username == user.username).first()           
                                         
            if query != None:
                #if user is found check his password
                if User.check_password(query.contrasena,user.contrasena):
                    #if correct, log in the user and return a user object
                    login_user(query)
                    return query 
                else:
                    return None
            else:
                return None
        except:
            flash("Error connecting to database, please try again later")
            return None
        
    @classmethod 
    def register_user(self, db, username, password, mail, realname = "", country = "", profile_img = None, token = "", active = False):
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
            if User.query.filter_by(username = username).first() is None or User.query.filter_by(mail = mail).first():
                           
                hashed_password = generate_password_hash(password)
                
                if profile_img.filename != "":
                
                    new_profile_img_name = upload_image(image=profile_img)
                
                privileges = Privileges(is_admin=False,can_comment=True,can_post=True)
                new_user = User(username=username,
                                contrasena=hashed_password,
                                realname=realname,
                                mail=mail,
                                country=country,
                                profileimg=new_profile_img_name,
                                token=token,
                                active=active,
                                privileges=privileges)
                db.session.add(new_user)
                db.session.commit()                            
                return new_user
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

    
    
    @classmethod
    def update_user(self, db, user_id, new_password = "", new_mail = "", new_real_name = "", new_country = "", new_profileimg = ""):

        user = User.query.get(user_id)
        if new_password != "":
            user.password = generate_password_hash(new_password)
        user.mail = new_mail
        user.realname = new_real_name
        user.country = new_country
    
        upload_image(user,new_profileimg)
        
        db.session.commit()
        return user
    
    