
from flask import flash,current_app
from .entities.User import User
from .entities.Privileges import Privileges
from werkzeug.security import generate_password_hash
from flask_login import login_user
import os
from utils.uploads import upload_image
from enum import Enum

class Rank(Enum):
    ZOMBIE="Zombie",
    SURVIVOR="Survivor",
    MODERATOR="Moderator"
    ADMIN="Admin"
    

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
                
                privileges = Privileges(is_admin=False,can_comment=True,can_post=True,rank = Rank.ZOMBIE.value)
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
                if user:
                    file_path, _ = os.path.split(current_app.config['UPLOADS_FOLDER'])
                    
                    try:
                        os.remove(os.path.join(current_app.config['UPLOADS_FOLDER'], user.profileimg))
                            
                    except FileNotFoundError as file_not_found:
                        print("File not found in " + file_path + ". " + str(file_not_found))

                    except Exception as ex:
                        print("Exception: " + str(ex))
                
                    db.session.delete(user)          

                    db.session.commit()
                else:
                    flash('User not found',category='general')
        except Exception as ex:
            print(ex)
            raise Exception(ex)

    
    
    @classmethod
    def update_user(self, db, user_id, new_password = None, new_mail = None, new_real_name = None, new_country = None, new_profileimg = None):

        user = User.query.get(user_id)
        if user:
            if new_password:
                user.password = generate_password_hash(new_password)
            if new_mail:
                user.mail = new_mail
            if new_real_name:
                user.realname = new_real_name
            if new_country:
                user.country = new_country
            if new_profileimg:
                upload_image(image= new_profileimg, user = user)
        
            db.session.commit()
    
            return user
        else:
            flash('No user found', category='general')
            return None
    
    