from flask import Blueprint, render_template, request, redirect, url_for, flash

from utils.database import db

from models.entities.Post import Post
from models.entities.Comment import Comment

from models.ModelPost import ModelPost
from models.ModelUser import ModelUser
from models.ModelComment import ModelComment

from flask_login import login_required, current_user

forum = Blueprint('forum',__name__, template_folder='templates')

#forum Config
latestPostsCount = 4


topicsDict = {
    "announcements": "fa-solid fa-bullhorn",
    "bugreports": "fa-solid fa-bug",
    "generaldiscussion": "fa-solid fa-comment",
    "media": "fa-solid fa-image"
}

class Topic: 
    def __init__(self, name, icon, count):
        self.name = name
        self.icon = icon
        self.count = count

@forum.route('/forumIndex')
def forumIndex():
    
    try:
        topicList = {}
        for topic in topicsDict:
            topicPosts = ModelPost.get_posts(topic = topic)
            topic = Topic(name=topic,icon=topicsDict[topic],count=len(topicPosts))    
            topicList[topic] = topic

        lastPosts = ModelPost.get_posts(limit=latestPostsCount) 
        return render_template('/forum/forum.html',
                            topicList = topicList,
                            lastPosts = lastPosts,)
    except Exception as ex:
        print(ex)
        #raise Exception(ex)
        flash("Error Connecting to database, please try again later",category='general')
        return redirect(request.referrer)
        
@forum.route('/posts/<topic>', methods=['GET', 'POST'])
@forum.route('/posts/<int:userID>', methods=['GET', 'POST'])

def posts(topic = None, userID = None):
    
    if userID != None:
        print("userID: " + str(userID))
        postsList = ModelPost.get_posts(user_id = userID)

    if topic != None:
        print("Topic:" + str(topic))
        postsList = ModelPost.get_posts(topic = topic)
    return render_template('/forum/posts.html',
            postsList = postsList,
            topic = topic,
            user_id = userID)
   
   
@forum.route('/create_post/<postTopic>', methods = ['GET','POST'])
@login_required
def create_post(postTopic):
    if request.method == 'POST':
        title = request.form['txtTitle']
        text = request.form.get('ckeditor')
        media = request.files['media']
        topic = postTopic
               
        modelPost = ModelPost.create_post(db,title,current_user.id,text,media,topic)    
                           
        return redirect(url_for('forum.showPost', id = modelPost.id))
      
    else:
        
        topic = postTopic
        
        return render_template("/forum/newPost.html", topic = topic)
    
@forum.route('/showPost/<int:id>')
def showPost(id):
    
    post = ModelPost.get_posts(post_id = id)
    return render_template("/forum/showPost.html",
                               post = post,)     
             
@forum.route('/postComment/<int:postID>', methods = ['POST'])
def postComment(postID):
    
    _text = request.form.get('ckeditor')
    _media = request.files['commentMedia']
    
        
    ModelComment.create_comment(db,postID,current_user.id,_text,_media)
         
    return redirect(url_for('forum.showPost',id = postID))        
       
@forum.route('/deletePost/<int:id>')
@login_required
def deletePost(id):
    
    try:
        post = Post.query.get(id)
        if post.user_id == current_user.id:
            ModelPost.delete_post(db,id)    
            flash("Post deleted successfully",category='general')
        else:
            flash("You are not allowed to delete this post",category='general')
    except Exception as ex:
        flash("An error ocurred when deleting Post",category='general')
        raise Exception(ex)
        
    return redirect(url_for('forum.forumIndex'))

@forum.route('/deleteComment/<int:id>')
@login_required
def deleteComment(id):
    try:
        comment = Comment.query.get(id)
        if comment.user_id == current_user.id:
            ModelComment.delete_comment(db,id)    
            flash("Comment deleted successfully",category='general')
        else:
            flash("You are not allowed to delete this comment", category='general')
    except Exception as ex:
        print(ex)
        flash("An error ocurred when deleting comment", category='general')
        
    return redirect(request.referrer)


