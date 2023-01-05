from flask import Blueprint, render_template, request, redirect, url_for, flash

from utils.db import db

from models.ModelPost import ModelPost
from models.ModelUser import ModelUser
from models.ModelComment import ModelComment

from flask_login import LoginManager, login_user, logout_user, login_required, current_user

from datetime import datetime

import os


forum = Blueprint('forum',__name__, template_folder='templates')



@forum.route('/forumIndex')
def forumIndex():
    
    try:
        announcementsCount = len(ModelPost.listPosts(db,'announcements')) 
        bugReportCount = len(ModelPost.listPosts(db,'bugreports'))
        generalDiscussionCount = len(ModelPost.listPosts(db,'generaldiscussion')) 
        mediaCount = len(ModelPost.listPosts(db,'media')) 
        
        
        #TODO: create func get latests posts
        #################################################
        latestPostsCount = 3

        allposts = ModelPost.listPosts(db)
            
        lastPosts = list(allposts[-latestPostsCount:]) 
        lastPosts.reverse()
        usersList = list()
        
        for post in lastPosts:
            
            postUser = ModelUser.get_User(db,post.user_ID)
            
            
            
            usersList.append(postUser)
        #################################################
        
        return render_template('/forum/forum.html',
                            announcementsCount = announcementsCount,
                            bugReportCount = bugReportCount,
                            generalDiscussionCount = generalDiscussionCount,
                            mediaCount = mediaCount,
                            lastPosts = lastPosts,
                            usersList = usersList)
    except Exception as ex:
        raise Exception(ex)
        #return redirect(url_for('index'))
        


@forum.route('/posts/<topic>', methods=['GET', 'POST'])
def showPosts(topic):
    
    postsList = ModelPost.listPosts(db,topic)

    usersList = list()

    commentsList = list()

    for post in postsList:
        
        postUser = ModelUser.get_User(db,post.user_ID)
        comments = ModelComment.getComments(db,post.id)        
        usersList.append(postUser)
        commentsList.append(comments)

    return render_template('/forum/posts.html',
            postsList = postsList, 
            topic = topic,
            usersList = usersList,
            commentsList = commentsList)
   
   
   
@forum.route('/createPost/<postTopic>', methods = ['GET','POST'])
@login_required
def createPost(postTopic):
    if request.method == 'POST':
        title = request.form['txtTitle']
        text = request.form['txtText']
        media = request.files['media']
        topic = postTopic

        now = datetime.now()

        date = now.strftime("%Y%H%M%S")
        
        
        if media.filename != '':
            mediaName = date + media.filename
            media.save("src/static/uploads/"+mediaName)
            
            modelPost = ModelPost.createPost(db,title,current_user.id,text,mediaName,topic)       
            
        else:
            modelPost = ModelPost.createPost(db,title,current_user.id,text,None,topic)
        post = list()
        post.append(modelPost)    
        user = ModelUser.get_User(db,modelPost.user_ID)
                    
        return render_template('/forum/showPost.html',
                               user = user, 
                               post = post,
                               comments = list())
      
    else:
        
        topic = postTopic
        
        return render_template("/forum/newPost.html", topic = topic)
    
@forum.route('/showPost/<int:id>')
def showPost(id):
    
    post = ModelPost.listPosts(db,None,id)
    if post != None:    
        user = ModelUser.get_User(db,post[0].user_ID) 
        
        comments = ModelComment.getComments(db,post[0].id)
        if comments != None:
            commentsUsers = list()
            for comment in comments:
                   commentUser = ModelUser.get_User(db,post[0].user_ID) 
                   commentsUsers.append(commentUser)
                   
            return render_template("/forum/showPost.html", 
                                   post = post, 
                                   user = user,
                                   comments = comments,
                                   commentsUsers = commentsUsers)
        
        
        else:
            return render_template("/forum/showPost.html",
                               post = post, 
                               user = user)     
    else:
        return render_template("/forum/posts.html")
             
@forum.route('/postComment/<int:postID>', methods = ['POST'])
def postComment(postID):
    
    _text = request.form['commentText']
    _media = request.files['commentMedia']
    
    
    ModelComment.createComment(db,postID,current_user.id,_text,_media)
    
    post = ModelPost.listPosts(db,None,postID)
    user = ModelUser.get_User(db,post[0].user_ID)
    comments = ModelComment.getComments(db,postID)
    commentsUsers = list()
    for comment in comments:
        commentUser = ModelUser.get_User(db,comment.user_ID)
        commentsUsers.append(commentUser)
     
    return redirect(url_for('forum.showPost',id = postID))        
    
    #return render_template('/forum/showPost.html',
    #                       post = post,
    #                       user = user,
    #                       comments = comments,
    #                       commentsUsers = commentsUsers)
    
    
    
@forum.route('/deletePost/<int:id>')
def deletePost(id):
    
    
    
    flash('Post deleted successfully')
    redirect(url_for('forum.forumIndex'))