from flask import Blueprint, render_template, request, redirect, url_for, flash

from utils.db import db

from models.ModelPost import ModelPost

from flask_login import LoginManager, login_user, logout_user, login_required, current_user

from datetime import datetime

import os


forum = Blueprint('forum',__name__, template_folder='templates')



@forum.route('/forumIndex')
def forumIndex():
    
    announcementsCount = len(ModelPost.listPosts(db,'announcements')) 
    bugReportCount = len(ModelPost.listPosts(db,'bugreports'))
    generalDiscussionCount = len(ModelPost.listPosts(db,'generaldiscussion')) 
    mediaCount = len(ModelPost.listPosts(db,'media')) 
    
    return render_template('/forum/forum.html',
                           announcementsCount = announcementsCount,
                           bugReportCount = bugReportCount,
                           generalDiscussionCount = generalDiscussionCount,
                           mediaCount = mediaCount)

@forum.route('/posts/<topic>', methods=['GET', 'POST'])
def posts(topic):
    selectedTopic = topic

    postslist = ModelPost.listPosts(db,topic)

    newPostlist = []
    for post in postslist:
        
        username = ModelPost.getPostUsername(db,post,2)
        
        listPost = list(post)
        
        listPost[2] = username[0]
        post = tuple(listPost)
        post = post
        print(post) 
        
        newPostlist.append(post)
    
    postslist = newPostlist    
    return render_template('/forum/posts.html',
            postslist = postslist, 
            selectedTopic = selectedTopic)
   
   
   
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
            media.save("src/static/Img/"+mediaName)
            modelPost = ModelPost.createPost(db,title,current_user.id,text,mediaName,topic)       
            postUser = modelPost.id
        else:
            modelPost = ModelPost.createPost(db,title,current_user.id,text,None,topic)
            postUser = modelPost.id

        return redirect(url_for('forum.showPost', username = postUser[0]))
  
    else:
        
        topic = postTopic
        
        return render_template("/forum/newPost.html", topic = topic)
    
@forum.route('/showPost/<int:id>')
def showPost(id):
    
    postList = ModelPost.listPosts(db,None,id)
    
    for post in postList:
        user = ModelPost.getPostUsername(db,post,2)
        username = user[0]
    
    
    return render_template("/forum/showPost.html" , postList = postList, username = username)

