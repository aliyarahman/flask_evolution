# -*- coding: utf-8 -*-

from flask import render_template, redirect
from app import app, db, lm  # Go get stuff we need from the app folder
from flask.ext.login import login_user, logout_user, login_required, current_user
from models import Post, User
from forms import NewUserForm, NewPostForm, LoginForm

@lm.user_loader
def load_user(userid):
    return User.query.get(userid)


@app.route('/')   # This means that this is the view for the landing page.					# 
@login_required
def index(): 
	users = User.query.all()
	posts = Post.query.all()
	return render_template('index.html', users = users, posts = posts)	# Now we load a template instead of just returning some text

@app.route('/login', methods = ['GET', 'POST'])	#Our login page
def login():
	form = LoginForm()
	if form.validate_on_submit():
        	user = form.get_user()
        	login_user(user)
		return redirect('/')
	return render_template('login.html', form = form)

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
@login_required
def add_post():
        form = NewPostForm()
        if form.validate_on_submit():
                post = Post()
                form.populate_obj(post)
                post.author_id = current_user.id
                db.session.add(post)
                db.session.commit()
                return redirect('/')
        return render_template("add_post.html", form = form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/login")

