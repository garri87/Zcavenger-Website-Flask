from .entities.Post import Post
from .entities.Comment import Comment

from datetime import datetime

import os

class ModelPost():
    
    @classmethod
    def create_post(self,db,title,user_ID,text,media,topic):
        try:

            createdate = datetime.now()
            
            fileDate = createdate.strftime("%Y%H%M%S")
            
            if media.filename != '':
                mediaName = fileDate + "_" + media.filename
                media.save("src/uploads/"+mediaName)
            else:
                mediaName = media
                
            post = Post(None,title,user_ID,createdate,text,mediaName,topic)
            
            db.session.add(post)
            db.session.commit()
                         
            return post
            
        except Exception as ex:
            raise Exception(ex)
        
        
   
    @classmethod
    def list_posts(self, postID = None, userID = None, topic = None, limit = 0):
        """returns a list of Post() objects by topic or id or all if no argument is given"""
        #try:
        if postID != None:
            postsList = Post.query.get(postID)
            
        elif topic != None: #search by topic
            postsList = Post.query.filter_by(topic = topic).all()
        elif userID != None: #search by user id
            postsList = Post.query.filter_by(user_ID = userID).all()
        else: #search all posts
            postsList = Post.query.all()
                
        if limit > 0:
            postsList = Post.query.order_by(Post.createdate.desc()).limit(limit).all()
               
        return postsList
        
        #except:
           # print('no Post found')
            #postlist = None
           # return postlist
        
    @classmethod
    def delete_post(self,db,id):
        try:
            post = Post.query.get(id)
                        
            if post != None and post.media != "":
                    try:
                        os.remove('src/uploads/' + post.media)
                        
                    except:
                        pass
                       # print('File: ' + post.media + ' not found in uploads directory')
                       
                            
            
            db.session.delete(post)
            db.session.commit()
            
            comments = Comment.query.filter_by(post_ID = id).all()
            
            for comment in comments:
                if comment.media != "":
                    try:
                        os.remove('src/uploads/' + comment.media)
                    except:
                        pass
                      #  print('File: ' + comment.media + ' not found in uploads directory')
                    
            db.session.delete(comments)
            db.session.commit()            
            
        except Exception as ex:
            raise Exception(ex)
            #print("No post found with ID: " + id)
            