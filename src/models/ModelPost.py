from .entities.Post import Post

from datetime import datetime


class ModelPost():
    
    @classmethod
    def createPost(self,db,title,user_ID,text,media,topic):
        try:
            cursor = db.connection.cursor()
            
            createdate = datetime.now()
            
            data = (title,user_ID,createdate,text,media,topic)
            
            sql = "INSERT INTO posts VALUES (NULL,%s,%s,%s,%s,%s,%s)"
            
            cursor.execute(sql,data)
            
            sql2 = "SELECT * FROM posts ORDER BY id DESC LIMIT 1"
            
            cursor.execute(sql2)
            
            post_ID = cursor.fetchone()    

            db.connection.commit()
            
            id = post_ID[0] 
             
            post = Post(id,title,user_ID,createdate,text,media)
            return post
            
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def listPosts(self,db,topic = None, id = None):
        
        try:
            cursor = db.connection.cursor()
            if id == None:
                sql = "SELECT * FROM zcavengerdb.posts WHERE topic = '{}';".format(topic)
            else:
                sql = "SELECT * FROM zcavengerdb.posts WHERE id = '{}';".format(id)
            
            cursor.execute(sql)
            
            postlist = cursor.fetchall()
                       
            db.connection.commit()
                                               
            return list(postlist)
        
        except:
            print('no Post found')
            postlist = None
            return list(postlist)
        
    @classmethod
    def getPostUsername(self,db,post,userIDIndex):
        
        cursor = db.connection.cursor()
        
        sql = "SELECT username FROM users WHERE id='{}'".format(post[userIDIndex])
         
        cursor.execute(sql)
        
        username = cursor.fetchone()
        
        db.connection.commit()
        
        return username