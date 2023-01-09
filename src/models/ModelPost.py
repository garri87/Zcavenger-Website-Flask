from .entities.Post import Post
from utils.db import db

from datetime import datetime

import os

class ModelPost():
    
    @classmethod
    def createPost(self,db,title,user_ID,text,media,topic):
        try:
            conn = db.connect()
            cursor = conn.cursor()
            
            createdate = datetime.now()
            
            fileDate = createdate.strftime("%Y%H%M%S")
            
            if media.filename != '':
                mediaName = fileDate + "_" + media.filename
                media.save("src/uploads/"+mediaName)
            else:
                mediaName = media
                
            data = (title,user_ID,createdate,text,mediaName,topic)
            
            sql = "INSERT INTO posts VALUES (NULL,%s,%s,%s,%s,%s,%s)"
            
            cursor.execute(sql,data)
            
            sql2 = "SELECT * FROM posts ORDER BY id DESC LIMIT 1"
            
            cursor.execute(sql2)
            
            post_ID = cursor.fetchone()    

            db.commit()  
            
            id = post_ID[0] 
             
            post = Post(id,title,user_ID,createdate,text,media,topic)
            return post
            
        except Exception as ex:
            raise Exception(ex)
        
        
   
    @classmethod
    def listPosts(self,db,topic = None, id = None):
        """returns a list of Post() objects by topic or id or all if no argument is given"""
        try:
            conn = db.connect()
            cursor = conn.cursor()
            if id == None and topic != None: #search by topic
                query = "SELECT * FROM zcavengerdb.posts WHERE topic = '{}';".format(topic)
            elif topic == None and id != None: #search by id
                query = "SELECT * FROM zcavengerdb.posts WHERE id = '{}';".format(id)
            elif topic == None and id == None: #search all posts
                query = "SELECT * FROM zcavengerdb.posts"
            
            cursor.execute(query)
            
            queryResult = cursor.fetchall()
                       
            conn.commit()
            
            postsList = list()
                                     
            for row in queryResult:
                post = Post(row[0], row[1], row[2], row[3],row[4],row[5],row[6])               
                
                postsList.append(post)
                      
                                               
            return postsList
        
        except:
            print('no Post found')
            postlist = None
            return list(postlist)
        
    @classmethod
    def deletePost(self,db,id):
        try:
            conn = db.connect()
            cursor = conn.cursor()
            
            queryPostMedia = "SELECT media FROM posts WHERE id = {}".format(id)
            
            cursor.execute(queryPostMedia)
            
            postMediaResult = cursor.fetchall()
            
            if postMediaResult != None:
                for row in postMediaResult:
                    try:
                        os.remove('src/uploads/' + row[0])
                        
                    except:
                        print('File: ' + row[0] + ' not found in uploads directory')
                    
                    
            queryDeletePost = "DELETE FROM posts WHERE id = {}".format(id)
            
            cursor.execute(queryDeletePost)    
            
            queryCommentsMedia = "SELECT media FROM comments WHERE id = {}".format(id)
            
            cursor.execute(queryCommentsMedia)
            
            commentMediaResult = cursor.fetchall()
            
            if commentMediaResult != None:
                for row in commentMediaResult:
                    try:
                        os.remove('src/uploads/' + row[0])
                        
                    except:
                        print('File: ' + row[0] + ' not found in uploads directory')
                        
            queryDeleteComments = "DELETE FROM comments WHERE post_ID = {}".format(id)
            
            cursor.execute(queryDeleteComments)
            
            conn.commit()
        
        except Exception as ex:
            raise Exception(ex)
            #print("No post found with ID: " + id)
            