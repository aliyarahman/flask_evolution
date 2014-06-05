# -*- coding: utf-8 -*-

from flask import render_template, redirect
from app import app, db  # Go get stuff we need from the app folder
from models import Post, User
from forms import NewUserForm, NewPostForm

@app.route('/')   # This means that this is the view for the landing page.					# 
def index(): 
	users = User.query.all()
	posts = Post.query.all()
	return render_template('index.html', users = users, posts = posts)	# Now we load a template instead of just returning some text

@app.route('/add_user', methods = ['GET', 'POST'])
def add_user():
        form = NewUserForm()
        if form.validate_on_submit():
                user = User()
                form.populate_obj(user)
                db.session.add(user)
                db.session.commit()
                return redirect('/')
        return render_template("add_user.html", form = form)

@app.route('/add_post', methods = ['GET', 'POST'])
def add_post():
        form = NewPostForm()
        if form.validate_on_submit():
                post = Post()
                form.populate_obj(post)
                db.session.add(post)
                db.session.commit()
                return redirect('/')
        return render_template("add_post.html", form = form)

