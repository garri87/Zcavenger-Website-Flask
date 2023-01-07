
from .entities.User import User
from werkzeug.security import generate_password_hash

from datetime import datetime

import os

class ModelUser():
    @classmethod
    def login(self, db, user):
        """Returns a User() object if credentials are correct"""
        try:
            cursor = db.connection.cursor()
            sql = """SELECT * FROM users 
            WHERE username = '{}'""".format(user.username)
            cursor.execute(sql)
            row = cursor.fetchone()
                        
            if row != None:
                user = User(row[0], row[1], User.check_password(row[2], user.contrasena),row[3], row[4], row[5], row[6], row[7],row[8], row[9])
                return user
            else:
                return None
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def registerUser(self, db, user, password, mail,realname = "", country = "", profileimg = "", token = "", active = False):
        try:
            cursor = db.connection.cursor()
            
            hashed_password = generate_password_hash(password)
            
            now = datetime.now()
            
            createdate = now.strftime("%Y%H%M%S")
            
            if profileimg != "":
                newprofileimg = createdate + profileimg.filename
                profileimg.save("src/uploads/" + newprofileimg)
            else:
                newprofileimg = ""
            
            data = (user,hashed_password,realname,mail,country,now,newprofileimg)
            sql = "INSERT INTO users (id, username, contrasena, realname, mail, country, createdate, profileimg) VALUES (NULL,%s,%s,%s,%s,%s,%s,%s)"
            cursor.execute(sql,data)
        
            sql2 = "SELECT * FROM users ORDER BY id DESC LIMIT 1"
            
            cursor.execute(sql2)
            
            row = cursor.fetchone() 
            
            
            db.connection.commit()
        
            return User(row[0],row[1],User.check_password(row[2], password),row[3],row[4],row[5],row[6],row[7])
        
        
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod    
    def checkAvailability(self, db, username = "", email = ""):
        try:
            cursor = db.connection.cursor()
            cursor.execute("SELECT username, mail FROM users WHERE username = '{}' AND mail = '{}'".format(username, email))
            row = cursor.fetchone()
            if row != None:
                if row[0] == username or row[1] == email:
                    return False
                else:
                    return True
            else:
                return True
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def get_User(self, db, id = None ,username="", email = ""):
        """return a User() object by user id, username or email"""
        
        try:
            cursor = db.connection.cursor()
            if id != None:
                sql = "SELECT * FROM users WHERE id = {}".format(id)
            elif username != "":
                sql = "SELECT * FROM users WHERE username = '{}'".format(username)
            elif email != "":
                sql = "SELECT * FROM users WHERE mail = '{}'".format(email)
            cursor.execute(sql)
            row = cursor.fetchone()
            if row != None:
                return User(row[0], row[1], row[2], row[3], row[4], row[5],row[6],row[7],row[8])
            else:
                return User(id = 0, username = "User Not Found", profileimg = "NoProfile.png")  
        except:
            
            return User(id = 0, username = "User Not Found", profileimg = "NoProfile.png")


    @classmethod
    def activateUser(self,db,id,activate):
        try:
            cursor = db.connection.cursor()
            sql = "UPDATE users SET active = {} WHERE id = {}".format(activate, id)
            cursor.execute(sql)
            db.connection.commit()

        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def deleteUser(self,db,id):   
        try:
            user = ModelUser.get_User(db,id)
            
            if user.profileimg != "":
                os.remove('src/uploads/' + user.profileimg)
            
            cursor = db.connection.cursor()
            
            sql = "DELETE FROM users WHERE id = {}".format(user.id)

            cursor.execute(sql)
            db.connection.commit()
           
            
            
        except Exception as ex:
            raise Exception(ex)

    