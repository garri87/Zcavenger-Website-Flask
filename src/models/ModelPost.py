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
             
            post = Post(id,title,user_ID,createdate,text,media,topic)
            return post
            
        except Exception as ex:
            raise Exception(ex)
        
        
   
    @classmethod
    def listPosts(self,db,topic = None, id = None):
        """returns a list of Post() objects by topic or id or all if no argument is given"""
        try:
            cursor = db.connection.cursor()
            if id == None and topic != None: #search by topic
                query = "SELECT * FROM zcavengerdb.posts WHERE topic = '{}';".format(topic)
            elif topic == None and id != None: #search by id
                query = "SELECT * FROM zcavengerdb.posts WHERE id = '{}';".format(id)
            elif topic == None and id == None: #search all posts
                query = "SELECT * FROM zcavengerdb.posts"
            
            cursor.execute(query)
            
            queryResult = cursor.fetchall()
                       
            db.connection.commit()
            
            postsList = list()
                                     
            for row in queryResult:
                post = Post(row[0], row[1], row[2], row[3],row[4],row[5],row[6])               
                
                postsList.append(post)
                      
                                               
            return postsList
        
        except:
            print('no Post found')
            postlist = None
            return list(postlist)