
from .entities.Comment import Comment

import os

from datetime import datetime


class ModelComment():
    @classmethod
    def create_comment(self,db,post_ID,user_ID,text,media = ""):
        """Inserts data in the comments table and returns a Comment() object"""
        try:
            
            now = datetime.now()
            
            fileDate = now.strftime("%Y%H%M%S")
            
            if media.filename != "":
                newMedia = fileDate + media.filename
                media.save("src/uploads/" + newMedia)
            else:
                newMedia = ""
            
            newComment = Comment(post_ID,user_ID,text,newMedia)
            
            db.session.add(newComment)
            db.session.commit()
            
                                   
            return newComment
            
        except Exception as ex:
            raise Exception(ex)
    
    
    @classmethod
    def get_comments(self, postID = None,userID = None):
        """returns a list of Comment() objects by post_ID or user_ID"""
        
        commentList = list()
        
        if postID is not None: 
            comments = Comment.query.filter(Comment.post_id == postID).order_by(Comment.createdate.desc())
            
        elif userID is not None:
            comments = Comment.query.filter(Comment.user_id == userID).order_by(Comment.createdate.desc()) 
               
        else:
            comments = Comment.query.all().order_by(Comment.createdate.desc()) 
                                                   
        return comments
    
    @classmethod
    def delete_comment(db,id):
        try:
            comment = Comment.query.get(id)
        
            if comment.media != "":
                os.remove('src/uploads/' + comment.media)

            db.session.delete(comment)
            db.session.commit()
            
        except Exception as ex:
            raise Exception(ex)
        
        
    