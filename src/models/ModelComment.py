from flask import current_app, flash
from .entities.Comment import Comment

import os

from datetime import datetime


class ModelComment():
    @classmethod
    def create_comment(self,db,post_id,user_id,text,media = ""):
        """Inserts data in the comments table and returns a Comment() object"""
        try:
            
            now = datetime.now()
            
            fileDate = now.strftime("%Y%H%M%S")
            
            if media.filename != "":
                newMedia = fileDate + media.filename
                media.save("src/uploads/" + newMedia)
            else:
                newMedia = ""
            
            newComment = Comment(post_id,user_id,text,newMedia)
            
            db.session.add(newComment)
            db.session.commit()
            
                                   
            return newComment
            
        except Exception as ex:
            raise Exception(ex)
    
    
    @classmethod
    def get_comments(self, postID = None,userID = None):
        """returns a list of Comment() objects by post_id or user_id"""
        
        
        if postID is not None: 
            comments = Comment.query.filter(Comment.post_id == postID).order_by(Comment.createdate.desc())
            
        elif userID is not None:
            comments = Comment.query.filter(Comment.user_id == userID).order_by(Comment.createdate.desc()) 
               
        else:
            comments = Comment.query.all().order_by(Comment.createdate.desc()) 
                                                   
        return comments
    
    @classmethod
    def delete_comment(self,db,id):
        try:
            comment = Comment.query.get(id)
            if comment:
                file_path, _ = os.path.split(current_app.config['UPLOADS_FOLDER'])

                if comment.media != "":
                    try:
                        os.remove(os.path.join(current_app.config['UPLOADS_FOLDER'], comment.media))
                            
                    except FileNotFoundError as file_not_found:
                        print("File not found in " + file_path + ". " + str(file_not_found))

                    except Exception as ex:
                        print("Exception: " + str(ex))

                db.session.delete(comment)
                db.session.commit()
            else:
                flash('Comment not found', category='general')
            
        except Exception as ex:
            raise Exception(ex)
        
        
    