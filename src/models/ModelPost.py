from .entities.Post import Post
from .entities.Comment import Comment
from models.ModelComment import ModelComment
from .entities.User import User

from datetime import datetime

import os

class ModelPost():
    
    @classmethod
    def create_post(self,db,title,user_id,text,media,topic):
        try:

            createdate = datetime.now()
            
            fileDate = createdate.strftime("%Y%H%M%S")
            
            if media.filename != '':
                mediaName = fileDate + "_" + media.filename
                media.save("src/uploads/"+mediaName)
            else:
                mediaName = None
                
            post = Post(title,user_id,text,mediaName,topic)
            
            db.session.add(post)
            db.session.commit()
                         
            return post
            
        except Exception as ex:
            raise Exception(ex)
        
        
   
    @classmethod
    def get_posts(self, post_id = None, user_id = None, topic = None, limit = 0):
        """returns a list of Post() objects by topic or id or all if no argument is given"""
        #try:
        if post_id:
            posts = Post.query.get(post_id)  
        elif topic: #search by topic
            posts = Post.query.filter(Post.topic == topic)
        elif user_id: #search by user id
            posts = (Post.query.join(User).filter(User.id == user_id)
                .all())
        else: #search all posts
            posts = Post.query.all()
        if limit > 0:
            posts = Post.query.order_by(Post.createdate.desc()).limit(limit).all()
               
        return posts
        
        #except:
           # print('no Post found')
            #postlist = None
           # return postlist
        
    @classmethod
    def delete_post(self,db,id):
            post = Post.query.get(id)
                        
            if post: 
                if post.media:
                    try:
                        os.remove('src/uploads/' + post.media)
                        
                    except Exception as ex:
                        print('File: ' + str(post.media) + ' not found in uploads directory ' + str(ex))
                        pass
                
                       
                comments = Comment.query.filter_by(post_id = id).all()
                if comments != None:
                    for comment in comments:
                        ModelComment.delete_comment(db,comment.id)
                    
                db.session.delete(post)
                db.session.commit()    
            else:
                print("Post not found with id " + str(id))   
