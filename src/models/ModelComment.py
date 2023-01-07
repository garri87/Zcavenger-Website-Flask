
from .entities.Comment import Comment

from datetime import datetime


class ModelComment():
    @classmethod
    def createComment(self,db,post_ID,user_ID,text,media = ""):
        """Inserts data in the comments table and returns a Comment() object"""
        try:
            cursor = db.connection.cursor()
            
            now = datetime.now()
            
            createdate = now.strftime("%Y%H%M%S")
            
            if media.filename != "":
                newMedia = createdate + media.filename
                media.save("src/uploads/" + newMedia)
            else:
                newMedia = ""
            
            data = (post_ID,user_ID,text,newMedia,now)
            
            sql = "INSERT INTO comments VALUES (NULL,%s,%s,%s,%s,%s)"
            cursor.execute(sql,data)
            
            sql2 = "SELECT * FROM comments ORDER BY id DESC LIMIT 1"
            
            cursor.execute(sql2)
            
            result = cursor.fetchone()    
            
            comment = Comment(result[0],result[1],result[2],result[3],result[4],result[5])
            db.connection.commit()
            
            return comment
            
        except Exception as ex:
            raise Exception(ex)
    
    
    @classmethod
    def getComments(self, db, post_ID = None,user_ID = None):
        """returns a list of Comment() objects by post_ID or user_ID"""
        cursor = db.connection.cursor()
        
        if post_ID != None and user_ID == None:
        
            sql = "SELECT * from comments WHERE post_ID = {}".format(post_ID)
        
        elif post_ID == None and user_ID != None:
            sql = "SELECT * from comments WHERE user_ID = {}".format(user_ID)
        
        cursor.execute(sql)
                
        result = cursor.fetchall()    
        comments = list()
        for row in result:
           comment = Comment(row[0],row[1],row[2],row[3],row[4],row[5])
           comments.append(comment)
        return comments
    
    @classmethod
    def deleteComment():
        return
    